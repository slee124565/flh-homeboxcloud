from __future__ import unicode_literals

from django.db import models

from datetime import datetime

# Create your models here.
class Report(models.Model):
    prodcut = models.CharField('product name', max_length=40,default='')
    hardware = models.CharField('pi hardware', max_length=20,default='')
    revision = models.CharField('pi revision', max_length=20,default='')
    serial = models.CharField('pi serial', max_length=20,default='')
    public_ip = models.CharField('public ip address', max_length=20,default='')
    private_ip = models.CharField('private ip address', max_length=40,default='')
    last_update = models.DateTimeField('last update time',default=datetime.now)
    status = models.CharField('system status',max_length=40,default='')
    version = models.CharField('sw version', max_length=40,default='')
    pub_key = models.CharField('public key', max_length=500,default='')
