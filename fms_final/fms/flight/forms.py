# forms.py
from django import forms
from .models import *

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'dob', 'cnic', 'phone', 'email', 'address']

class NewComplaint(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'email', 'subject', 'message']
