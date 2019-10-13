from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import *
import bcrypt

def index(request):
    return render(request,'login_app/index.html')


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
        return redirect('/registered')
    return redirect('/')


def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key,val in errors.items():
            messages.error(request, val)
    else:
        user = User.objects.get(email=request.POST['login_email'])
        request.session['logged_in'] = user.id
        return redirect('/success')
    return redirect('/')


def success(request):
    status = ''
    if User.objects.get(id=request.session['logged_in']) == User.objects.last():
        status = "logged in"
    else: 
        status = 'not logged in'
    context = {'user': User.objects.get(id=request.session['logged_in']), 'status': status}
    return render(request, 'login_app/success.html', context)


def registered(request):
    return render(request,'login_app/registered.html')


def view_wall(request):
    context = {
        'user': User.objects.get(id=request.session['logged_in']),
        'messages': Message.objects.all(),
    }
    return render(request,'login_app/wall.html',context)


def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('/')

def post_message(request, user_id):
    user = User.objects.get(id=user_id)
    print(user.id)
    Message.objects.create(message = request.POST['message_post'],user = user)
    return redirect('/wall')


def post_comment(request, message_id):
    user = User.objects.get(id=request.session['logged_in'])
    message = Message.objects.get(id=message_id)
    new = Comment.objects.create(comment=request.POST['comment_post'],user = user, message = message)
    print(new.comment)
    return redirect('/wall')