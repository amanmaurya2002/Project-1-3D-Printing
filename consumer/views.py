from django.shortcuts import render, redirect
from .forms import NewUserForm, Part
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    return render(request,'consumer/home.html')

def about(request):
    return render(request, 'consumer/about.html')

# Ask for user registration details and save it in database.
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="consumer/register.html", context={"register_form":form})

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
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="consumer/login.html", context={"login_form":form})

# Logout user
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

# Lets user upload the model to print
def print(request):
    if request.method == 'POST':
        form = Part(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('print')
    else:
        form = Part()
    return render(request, 'consumer/print.html', {'upload_form': form})