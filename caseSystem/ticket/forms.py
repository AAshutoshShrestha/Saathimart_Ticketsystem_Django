from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Workers,Case,Employe


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User		
		fields = ['username', 'email', 'password1', 'password2']

        
class WorkersForm(ModelForm):
	class Meta:
		model = Workers		
		fields = '__all__'			#for all model fields
		exclude = ['user']
		
class EmployeForm(ModelForm):
	class Meta:
		model = Employe
		fields = '__all__'
		exclude = ['user']

class CaseForm(ModelForm):
	class Meta:
		model = Case
		fields = ['user','topic','description','Category','Department','Priority','Status','note']






