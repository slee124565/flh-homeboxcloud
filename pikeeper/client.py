from django.core import signing
from django.conf import settings

import pikeeper
import requests
import logging

logger = logging.getLogger(__name__)

def get_status_report_v1():
    '''get device status report v1 including:
    version, cpu_info, local_ip_address, public key, service list'''
    
    status_report = {
        'version': 'v1.0',
        'cpu_info': pikeeper.get_cpu_info(),
        'local_ip': pikeeper.get_local_ip(),
        'public_key': pikeeper.get_public_key(),
        'services': pikeeper.get_service_name_list()
        }
    logger.debug('status_report: %s' % str(status_report))
    
    return status_report

def get_encrypted_status_report(version='v1.0'):
    '''encrypt report data'''
    
    if version == 'v1.0':
        report = get_status_report_v1()
    else:
        raise Exception('')
    
    encrypted_data = signing.dumps(obj=report,salt='django.core.signing')
    logger.debug('encrypted status report: %s' % encrypted_data)
    return encrypted_data

def post_status_report_to_server():
    '''http post encrypted status report (json object) to server'''
    api_path = 'https://home-box.appspot.com/api/v1/report/'
    
    try:
        encrypt_report = get_encrypted_status_report(version='v1.0')
        r = requests.post(api_path,data={'data': encrypt_report})
        logger.info('http post response: %s, %s' % (r.status_code,r.text))
        if r.status_code != 200:
            logger.warning('post_status_report_to_server response code exception')
    except:
        logger.error('post_status_report_to_server exception', exc_info=True)