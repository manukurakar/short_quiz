from django.db import models
from django.utils import timezone as tz


# Create your models here.

class students(models.Model):
    mobile_no = models.TextField(max_length=20,default=None, null=True)
    email = models.CharField(max_length=100, default=None, null=True)
    join_date =  models.DateField(default=tz.now())
    name = models.CharField(max_length=200,default=None, null=True)
    location = models.CharField(max_length=200, default=None, null=True)
    school = models.CharField(max_length=200, default=None, null=True)
    dob = models.DateField(default='1899-12-31', null=True)
    zone = models.CharField(max_length=100,default=None, null=True)
    parent_contact = models.CharField(max_length=100,default=None, null=True)
    mother_name = models.CharField(max_length=200,default=None, null=True)
    volunteer = models.CharField(max_length=10,default=None, null=True)
    is_member = models.CharField(max_length=10,default=None, null=True)


    def __unicode__(self):
        return self.mobile_no


class studentResponse(models.Model):
    mobile_no = models.TextField(max_length=20, default=None, null=True)
    quiz_id = models.CharField(max_length=100)
    attempted_date = models.DateField(default=tz.now())
    marks = models.DecimalField(max_digits=6,decimal_places=2)
    student_response = models.TextField()

    def __unicode__(self):
        return self.mobile_no




