from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm
#from django.contrib.auth.models import User
#table from auth class table from models user is replica of main user

from django.contrib.auth import login,logout,authenticate

from django.utils.http import is_safe_url
from django.contrib.auth import get_user_model
User = get_user_model()

def logout_page(request):
    logout(request)
    return redirect("home")

def login_page(request):
    login_form = LoginForm(request.POST or None)
    redirect_url=request.POST.get("red_url",None)
    context ={'form':login_form}

    if login_form.is_valid():
        un=login_form.data.get("email")
        pwd=login_form.data.get("pwd")
        user=authenticate(username=un,password=pwd)

        if user:
            login(request,user)
            if redirect_url:
                if is_safe_url(redirect_url,request.get_host()):
                    return redirect(redirect_url)
            return redirect("home")
        else:
            context['msg']="Invalid Credentials"
    return render(request,"accounts/login.html",context)        
        



# Create your views here.

def register_page(request):
    # print(request_POST)

    register_form=RegistrationForm(request.POST or None)
    context={'form':register_form}
    #if request.methhod=='POST':
    #   re

    if register_form.is_valid():
        
        fn=register_form.cleaned_data.get('fullname')
        mob=register_form.cleaned_data.get('mobile')
        pwd=register_form.cleaned_data.get('pwd')
        email=register_form.cleaned_data.get('email')
        user=User.objects.create_user(email=email,password=pwd,full_name=fn,mobile=mob)

        if user:
            context['msg']="User Created.........!"

    return render(request,'accounts/register.html',context)
    
