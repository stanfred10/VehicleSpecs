from django import forms
from django.forms import ModelForm
from django import forms
from .models import *

class OwnerForm(forms.ModelForm):

    class Meta:
        model = Owner
        fields = '__all__'

class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = '__all__'