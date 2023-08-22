from django.shortcuts import render
from .models import Team
# Create your views here.

# creating home function
def home(request):
    teams = Team.objects.all()
    data = {
        'teams':teams
    }

    return render(request,'pages/home.html',data)

# creating about function
def about(request):
    teams = Team.objects.all()
    data = {
        'teams':teams
    }
    return render(request,'pages/about.html',data)

#creating services function
def services(request):
    return render(request,'pages/services.html')

#creating contact function
def contact(request):
    return render(request,'pages/contact.html')

