from django.forms import ModelForm
from django import forms
from .models import employee

class empForm(ModelForm):
    class Meta:
        model = employee
        fields = "__all__"