from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.html import TRAILING_PUNCTUATION_CHARS
from .models import Part
from project1.models import PrintSpecification, ShippingInfo


# Create your forms here.

# Form for new user registration
class NewUserForm(UserCreationForm):
	#email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("first_name", "last_name", "username", "email", "password1", "password2")


# Form for uplading a part
class PartUploadForm(ModelForm):
	class Meta:
		model = Part
		fields = ["part"]

# Form for uplading a part
class UploadForm(forms.Form):
	file = forms.FileField(required=True)

class PrintSpecificationForm(ModelForm):
	class Meta:
		model = PrintSpecification
		fields = ['resolution', 'process', 'material', 'colour', 'additional_info']

class ShippingInfoForm(ModelForm):
	class Meta:
		model = ShippingInfo
		fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'pin_code', 'city']