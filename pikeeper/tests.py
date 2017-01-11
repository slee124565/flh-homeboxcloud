from django.test import TestCase

# Create your tests here.
import pikeeper
import pikeeper.client as piclient
import time

class PiKeeperClientTestCase(TestCase):
    def setUp(self):
        pass
    
    def test_get_status_report_v1(self):
        '''get_status_report_v1 should has entry (version, v1.0)'''
        report  = piclient.get_status_report_v1()
        self.assertEqual(report['version'], 'v1.0',
                            'Report version should be v1.0.')
        
    def test_get_encrypted_status_report(self):
        '''get_encrypted_status_report should has different encrypted
        data each time executed'''
        en_data_1 = piclient.get_encrypted_status_report()
        time.sleep(2)
        en_data_2 = piclient.get_encrypted_status_report()
        self.assertNotEqual(en_data_1, en_data_2,
                            'It should product different encrypted data.')

class PiKeeperTestCase(TestCase):
    def setUp(self):
        pass
    
    def test_get_service_name_list(self):
        '''get_service_name_list should return a list of service name enabled'''
        service_list = pikeeper.get_service_name_list()
        self.assertGreater(len(service_list), 0, 
                           'It should have at least one service name exist.')
        
    def test_get_public_key(self):
        '''get_public_key should return a string'''
        pub_key = pikeeper.get_public_key()
        self.assertNotEqual(pub_key, '', 
                            'It should have root public key information.')
        
    def test_get_cpu_info(self):
        '''get_cpu_info should return a dict with pi cpu_info object'''
        cpu_info = pikeeper.get_cpu_info()
        self.assertIsNot(cpu_info['hardware'], '', 
                         'It should have pi hardware information.')
        self.assertIsNot(cpu_info['revision'], '', 
                         'It should have pi revision information.')
        self.assertIsNot(cpu_info['serial'], '', 
                         'It should have pi serial information.')
        
    def test_get_local_ip(self):
        '''get_local_ip return a list of ip address'''
        local_ip_list = pikeeper.get_local_ip()
        self.assertGreater(len(local_ip_list), 0,  
                        'It should have IP address exist.')

    def test_get_encrypt_salt(self):
        '''get_encrypt_salt return none empty string'''
        self.assertNotEqual(pikeeper.get_encrypt_salt(), '',
                            'It should return none empty string.')
        
#     def test_post_status_report(self):
#         '''post_status_report should post a dict object for web server'''
#         status_report = post_status_report()
#         self.assertNotEqual(status_report.get('cpu_info'), None, 
#                             'It should have cpu_info information')
#         self.assertNotEqual(status_report.get('local_ip'), None, 
#                             'It should have local_ip information')
#         self.assertNotEqual(status_report.get('public_key'), None, 
#                             'It should have public_key information')
#         self.assertNotEqual(status_report.get('services'), None, 
#                             'It should have services information')
    
