from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.

# Home
def Home(request):
    return render(request,'blog/home.html')

# About
def About(request):
    return render(request,'blog/about.html')

# Contact
def Contact(request):
    return render(request,'blog/contact.html')

# dashboard
def Dashboard(request):
    return render(request,'blog/dashboard.html')

# login
def Loginfunc(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.error(request,"You have entered the wrong Username or Password")
    else:
        fm=AuthenticationForm()
    return render(request,'blog/login.html',{'form':fm})

# signup
def Signupfunc(request):
    if request.method=="POST":
        fm=Signupform(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request," Congratulation, Your profile has been Created !!!!")
            return redirect('login')
    else:
        fm=Signupform()
    return render(request,'blog/signup.html',{"form":fm})

# logout
def Logoutfunc(request):
    pass
    # return render(request,'blog/logout.html')