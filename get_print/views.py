from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm, PartUploadForm, PrintSpecificationForm
from .models import Part
from project1.util import find_suppliers

# Create your views here.

def home(request):
    return render(request,'get_print/home.html')

def about(request):
    return render(request, 'get_print/about.html')

# Ask for user registration details and save it in database.
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('get_print:workspace')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="get_print/register.html", context={"register_form":form})

# Verify credentials and login user
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('get_print:workspace')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name='get_print/login.html', context={'login_form':form})

# Logout user
@login_required
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('get_print:home')

# User's workspace: Parts, orders, history, profile.
@login_required
def workspace(request):
    return render(request, 'get_print/workspace.html')

# Show all parts Customer has uploaded
@login_required
def parts(request):
    parts = request.user.customer.parts.all()
    return render(request, 'get_print/parts.html', {'parts': parts})

# Lets user upload the model to print
@login_required
def upload_part(request):
    if request.method == 'POST':
        uploaded_part = PartUploadForm(request.POST, request.FILES)
        if uploaded_part.is_valid():
            p = uploaded_part.save()
            request.user.customer.parts.add(p)
            return redirect('get_print:parts')
    form = PartUploadForm()
    return render(request, 'get_print/upload_part.html', {'part_upload_form': form})

@login_required
def orders(request):
    pass

@login_required
def part(request, part_id):
    part_name = Part.objects.get(id=part_id).part.name
    form = PrintSpecificationForm()
    return render(request, 'get_print/part.html', {'print_specification_form': form, 'part_name': part_name})

@login_required
def quotes(request):
    specification = PrintSpecificationForm(request.POST).save()
    suppliers = find_suppliers(specification)
    return render(request, 'get_print/quotes.html', {'suppliers': suppliers}) 

@login_required
def order_status(request):
    status = 'Order placed!'
    return render(request, 'get_print/order_status.html', {'status': status})

@login_required
def projects(request):
    return render('get_print/projects.html')