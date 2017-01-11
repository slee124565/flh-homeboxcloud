from django.views.generic import View
from django.conf import settings
from django.core import signing
from django.http import HttpResponse, Http404

import logging
logger = logging.getLogger(__name__)

from .models import Report

class ApiReport_v1(View):

    def post(self, request, *args, **kwargs):
        try:
            encrypted_data = request.POST.get('data',None)
            logger.debug('encrypted_data digest: %s' % encrypted_data[:20])
            
            client_secret_key = settings.PIKEEPER['client_secret_key']
            client_report = signing.loads(encrypted_data,client_secret_key)
            logger.debug('client report keys: %s' % str(client_report.keys()))
            
            return HttpResponse('OK')
        except:
            logger.error('ApiReport_v1 post exception', exc_info=True)
            raise Http404
        
        