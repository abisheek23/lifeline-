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

def add_department(req):
    if 'admin'in req.session:
        if req.method == 'POST':
            name= req.POST['name']
            department.objects.create(name=name.lower())
            departments=department.objects.all()
            return render(req,'admin/add_department.html',{'departments':departments})
        else:
            departments=department.objects.all()
            return render(req,'admin/add_department.html',{'departments':departments})
    else:
        return redirect(login1)

def add_staff(req):
    if 'admin' in req.session:
        if req.method=='POST':
            file=req.FILES['image']
            name=req.POST['staff-name']
            staff_id=req.POST['staff-id']
            email=req.POST['staff-email']
            position=req.POST['position']
            depart=req.POST.get('department')
            try:
              departments=department.objects.get(pk=depart)
            except:
                departments=None
            data=Staff.objects.create(name=name,staff_id=staff_id,email=email,position=position,department=departments,img=file)
            data.save()
            return redirect(admin_home)
        else:
            depart=department.objects.all()
            return render(req,'admin/add_staff.html',{'depart':depart})
    else:
       return redirect(login1)
    
def view_staff(req):
    staffs=Staff.objects.all()
    return render(req,'admin/view_staff.html',{'staff':staffs})

 



def admin_home(req):
    if 'admin' in req.session:
        return render(req,'admin/adminhome.html')
    else:
        return redirect(login1)

# user

def user_home(req):
    if 'user' in req.session:
        return render (req,'user/user_home.html')