from django.db import models
from django.utils.timezone import now


# Create your models here.

class students(models.Model):
    mobile_no = models.TextField(max_length=20);
    enter_date =  models.DateField(default=now())

    def __unicode__(self):
        return self.mobile_no

