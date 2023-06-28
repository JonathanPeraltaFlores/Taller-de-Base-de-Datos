from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Cliente
from .models import Requerimiento
from .models import RequerimientoEspecif

class ClienteAddForm(forms.ModelForm):
	
	class Meta:
		model = Cliente
		exclude = ("user",)

class RequerimientoAddForm(forms.ModelForm):
    	
	class Meta:
		model = Requerimiento
		exclude = ("user",)

class RequerimientoEspecifAddForm(forms.ModelForm):
    	
	class Meta:
		model = RequerimientoEspecif
		exclude = ("user",)