from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import *
import bcrypt



def index(request):
    return render(request, 'login_app/index.html')


def register(request):
    print(User.objects.all().values())
    errors = User.objects.regValidator(request.POST)
    if len(errors) > 0:
        for key,val in errors.items():
            messages.error(request, val)
    else:
        password = request.POST['password']         
        hashpass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(first_name = request.POST['first'], last_name = request.POST['last'], email=request.POST['email'], password=hashpass)
        return redirect('/')
    return redirect('/')


def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key,val in errors.items():
            messages.error(request, val)
    else:
        user = User.objects.get(email=request.POST['login_email'])
        request.session['logged_in'] = user.id
        return redirect('/')
    return redirect('/')


def success(request):
    status = ''
    if User.objects.get(id=request.session['logged_in']) == User.objects.last():
        status = "logged in"
    else: 
        status = 'not logged in'
    return redirect('/')



