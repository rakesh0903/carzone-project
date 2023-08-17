from django.shortcuts import render

# Create your views here.

# creating home page
def home(request):
    return render(request,'pages/home.html')
