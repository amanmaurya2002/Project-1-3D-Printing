from django.forms import ModelForm
from .models import Part
from project1.models import PrintSpecification, ShippingInfo


# Create your forms here.

# Form for uplading a part
class PartUploadForm(ModelForm):
	class Meta:
		model = Part
		fields = ["part"]

class PrintSpecificationForm(ModelForm):
	class Meta:
		model = PrintSpecification
		fields = ['units', 'resolution', 'process', 'material', 'colours', 'additional_info']

class ShippingInfoForm(ModelForm):
	class Meta:
		model = ShippingInfo
		fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'pin_code', 'city']