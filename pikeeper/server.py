from django.views.generic import View
from django.conf import settings
from django.core import signing
from django.http import HttpResponse, Http404
from django.utils import timezone

import logging
logger = logging.getLogger(__name__)

from ipware.ip import get_real_ip
import json

from .models import Report

class ApiReport_v1(View):

    def post(self, request, *args, **kwargs):
        try:
            encrypted_data = request.POST.get('data',None)
            logger.debug('encrypted_data digest: %s' % encrypted_data[:20])
            
            secret_key = settings.PIKEEPER['client_secret_key']
            report = signing.loads(encrypted_data,secret_key)
            logger.debug('client report keys: %s' % str(report.keys()))
            rpi_serial = report.get('cpu_info',{}).get('serial',None)
            if not rpi_serial is None:
                db_entry,_ = Report.objects.get_or_create(serial=rpi_serial)
                db_entry.serial = rpi_serial
                db_entry.hardware = report.get('cpu_info',{}).get('hardware','')
                db_entry.revision = report.get('cpu_info',{}).get('revision','')
                public_ip = get_real_ip(request)
                if public_ip is None:
                    public_ip = ''
                db_entry.public_ip = public_ip
                db_entry.services = str(report.get('services',[]))
                db_entry.local_ip_list = str(report.get('local_ip',[]))
                db_entry.public_key = str(report.get('public_key',''))
                db_entry.last_update_time = timezone.now()
                db_entry.save()
                logger.info('ApiReport_v1: %s' % str(db_entry) )
            else:
                logger.warning('ApiReport_v1 no serial: %s' % json.dumps(report))
            
            return HttpResponse('OK')
        except:
            logger.error('ApiReport_v1 post exception', exc_info=True)
            raise Http404
        
        