from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact, Newuser

# Create your views here.
def index(request):
    return render(request ,'index.html')

def about(request):
    return render(request , 'about.html')

# Ask for user sign up details and save it in database.
def user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        Pwd = request.POST.get('Pwd')
        
        news = Newuser(name = name , email=email , Pwd=Pwd )
        news.save()
    return render(request , 'user.html')

# Ask for supplier information and save it in databse.
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name = name , email=email , phone=phone, date=datetime.today())
        contact.save()

    
    return render(request , 'contact.html')
