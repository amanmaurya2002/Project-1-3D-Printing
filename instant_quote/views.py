from django.shortcuts import render
from .forms import PartUploadForm, PrintSpecificationForm, ShippingInfoForm
from project1.util import find_suppliers

# Create your views here.
def index(request):
    upload_form = PartUploadForm()
    specification_form = PrintSpecificationForm()
    shipping_info_form = ShippingInfoForm()
    suppliers = []
    if request.method == 'POST':
        PartUploadForm(request.POST, request.FILES).save()
        specification = PrintSpecificationForm(request.POST).save()
        ShippingInfoForm(request.POST).save()
        suppliers = find_suppliers(specification)
    return render(request, 'instant_quote/index.html', {'upload_form': upload_form, 'specification_form': specification_form, 'shipping_info_form': shipping_info_form, 'suppliers': suppliers})