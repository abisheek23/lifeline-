from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import  User
from django.contrib import messages
from .models import *
import os

# Create your views here.

def login1(req):
    if 'admin' in req.session:
        return redirect(admin_home)
    if 'user' in req.session:
        return redirect (user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            if data.is_superuser:
              req.session['admin']=uname   #create session 
              return redirect(admin_home)
            else:
                req.session['user']=uname
                return redirect(user_home)
        else:
            messages.warning(req, " invalid user name or password")
            return redirect(login)
    else:
        return render(req,'login.html')
   

#    admin

def admin_home(req):
    if 'admin' in req.session:
        return render(req,'admin/adminhome.html')
    else:
        return redirect(login)

# user

def user_home(req):
    if 'user' in req.session:
        return render (req,'user/user_home.html')