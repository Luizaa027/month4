from django.shortcuts import render 
from aman.models import Setting 

# Create your views here.

def index(request):
    settings = Setttings.object.lates("id")
    return render(request, "index.html", locals()) 

def contacts(request):
    settings = Settings.object.lates("id")
    return render(request, "contacts.html",locals())

