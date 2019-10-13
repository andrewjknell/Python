from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'practice_app/index.html')


def log_reg(request):
    if request.POST['log_reg'] == 'login':
        errors = User.objects.loginValidator(request.POST)
        if len(errors) > 0:
            for key,val in errors.items():
                messages.error(request, val)
            
        else:
            user = User.objects.get(email=request.POST['login_email'])
            request.session['logged_in'] = user.id
            print(user.first_name)
            return redirect('/')
        return redirect('/')

    if request.POST['log_reg'] == 'register':
        print(User.objects.all().values())
        errors = User.objects.regValidator(request.POST)
        if len(errors) > 0:
            for key,val in errors.items():
                messages.error(request, val)
        else:
            password = request.POST['password']         
            hashpass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.objects.create(first_name = request.POST['first'], last_name = request.POST['last'], email=request.POST['email'], password=hashpass)
            print(user.first_name)
        return redirect('/')