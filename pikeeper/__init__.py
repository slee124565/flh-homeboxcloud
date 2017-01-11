
import os
from subprocess import check_output

import logging
logger = logging.getLogger(__name__)

def get_encrypt_salt():
    '''return device encrypt salt string'''
    
    return get_cpu_info()['serial']

def get_service_name_list():
    '''return enabled service name list'''
    
    services = []
    try:
        services = [ service for service in os.listdir('/etc/uwsgi/apps-enabled')]    
    except:
        logger.warning('get_service_name_list exception', exc_info = True)
    finally:
        return services
    
def get_public_key():
    '''return root ssh public key if exist'''
    
    shell_cmd = 'sudo cat /root/.ssh/id_rsa.pub'
    pub_key = ''
    try:
        if os.path.exists('/root/.ssh/id_rsa.pub'):
            pub_key = check_output(shell_cmd.split(' ')).decode().strip()
    except:
        logger.warning('get_public_key exception', exc_info = True)
    finally:
        return  pub_key    

def get_cpu_info():
    '''return raspberry pi json data from /proc/cpuinfo:
    {
        'hardware' : 'xxx',
        'revision': 'xxx',
        'serial' : 'xxx',
    } 
    '''
    try:
        cpuinfo = {
            'hardware': '',
            'revision': '',
            'serial': '',
            }
        if os.path.exists('/proc/cpuinfo'):
            with open('/proc/cpuinfo') as fh:
                for info in fh:
                    if info.startswith('Hardware'):
                        cpuinfo['hardware'] = (info.split(':')[-1]).strip()
                    if info.startswith('Revision'):
                        cpuinfo['revision'] = (info.split(':')[-1]).strip()
                    if info.startswith('Serial'):
                        cpuinfo['serial'] = (info.split(':')[-1]).strip()
            logger.debug('current cpuinfo: %s' % str(cpuinfo))            
        else:
            logger.warning('no /proc/cpuinfo file exist!')
    except:
        logger.error('get_cpu_info exception', exc_info=True)
    finally:
        return cpuinfo
    
def get_local_ip():
    '''return local ip address list'''
    ip_list = []
    try:
        local_ip = check_output(['hostname', '-I']).decode().strip()
        logger.debug('current local ip address %s' % local_ip)
        ip_list = local_ip.split(' ')
    except:
        logger.warning('get_local_ip fail', exc_info=True)
    finally:
        return ip_list
    
    
