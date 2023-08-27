from django.shortcuts import render,redirect

# Create your views here.

#login function base view
def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    return redirect('pages:home')

def register(request):
    return render(request,'accounts/register.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')
