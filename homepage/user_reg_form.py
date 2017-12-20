__author__ = 'kurakar'
from django import forms
from django.contrib.auth.models import User
import regex as re


class RegistrationForm(forms.ModelForm):
    mobile =  forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('mobile','password','first_name','last_name')

    def validate_mobile(self,phone):
        return re.match(r'^[789]\d{9}$',phone,flags=0)


    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if User.objects.filter(username=mobile).count():
            raise forms.ValidationError("Mobile Numbers Already Registered")
        if not self.validate_mobile(mobile):
            raise forms.ValidationError("Invalid Mobile Number")
        else:
            return mobile