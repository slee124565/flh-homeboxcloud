from django.db import models
from django.utils import timezone

# Create your models here.
class Report(models.Model):
    version = models.CharField('report version', max_length=10,default='v1.0')
    hardware = models.CharField('pi hardware', max_length=20,default='')
    revision = models.CharField('pi revision', max_length=20,default='')
    serial = models.CharField('pi serial', max_length=20,default='')
    public_ip = models.CharField('public ip', max_length=20,default='')
    last_update_time = models.DateTimeField('last update time',default=timezone.now)
    services = models.CharField('service list', max_length=100,default='')
    local_ip_list = models.CharField('local ip list', max_length=100,default='')
    public_key = models.CharField('public key', max_length=500,default='')
    
    def __unicode__(self):
        return str((self.version,
                    self.hardware,
                    self.revision,
                    self.serial,
                    self.public_ip,
                    str(self.local_ip_list),
                    str(timezone.localtime(self.last_update_time,
                                           timezone.get_default_timezone())),
                    str(self.services),
                    self.public_key[:15]+'...'+self.public_key[-30:]))