from django.shortcuts import render
from main.models import *

# Create your views here.

def index(request):
    contacts  = Contact.objects.all()
    return render(
        request, 
        "main/index.html",
        {'contacts': contacts})       
                
