from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from datetime import datetime
from consumer.models import Contact, Newuser

# Create your views here.

def home(request):
    return render(request,'consumer/home.html')

def about(request):
    return render(request, 'consumer/about.html')

# Ask for user registration details and save it in database.
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("consumer")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="consumer/register.html", context={"register_form":form})

# Verify credentials and login user
def login(request):
    return render(request, 'consumer/login.html')

# Ask for supplier information and save it in databse.
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name = name, email=email, phone=phone, date=datetime.today())
        contact.save()
    
    return render(request, 'consumer/contact.html')
