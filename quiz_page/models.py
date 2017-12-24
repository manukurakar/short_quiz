from django.db import models
from django.utils import timezone as tz
from datetime import timedelta

# Create your models here.

class quiz(models.Model):
    quiz_id = models.CharField(max_length=100,null=False)
    description = models.TextField()
    name = models.CharField(max_length=500,null=True,blank=True,default='Test')
    cat = models.CharField(max_length=100,default='GK')
    crt_dt = models.DateField(default=tz.now())
    exp_dt = models.DateField(default=tz.now() + timedelta(days=7))
    auth = models.CharField(max_length=100,null=False)
    questions = models.TextField()
    result_hold = models.BooleanField(default=None)
    timer_sec = models.IntegerField(default=600)

    def __unicode__(self):
        return self.id