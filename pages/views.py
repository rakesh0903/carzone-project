from django.shortcuts import render

# Create your views here.

# creating home function
def home(request):
    return render(request,'pages/home.html')

# creating about function
def about(request):
    return render(request,'pages/about.html')

#creating services function
def services(request):
    return render(request,'pages/services.html')

#creating contact function
def contact(request):
    return render(request,'pages/contact.html')

