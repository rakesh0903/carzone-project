from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.

#login function base view
def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    return redirect('pages:home')

def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username Already exist")
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email already exist")
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                    auth.login(request,user)
                    messages.success(request,"you are now log in")
                    return redirect('accounts:dashboard')
                    user.save()
                    messages.success(request,"You are register successfully.")
                    return redirect('accounts:login')
        else:
            messages.error(request,"password do not matching")
            return redirect('accounts:register')

        
    else:
        return render(request,'accounts/register.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

