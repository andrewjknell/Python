from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import *
import bcrypt



def index(request):
    return render(request, 'fave_book_app/index.html')


def log_reg(request):
    if request.POST['log_reg'] == 'login':
        errors = User.objects.loginValidator(request.POST)
        if len(errors) > 0:
            for key,val in errors.items():
                messages.error(request, val)
            
        else:
            user = User.objects.get(email=request.POST['login_email'])
            request.session['logged_in'] = user.id
            return redirect('/main')
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
            User.objects.create(first_name = request.POST['first'], last_name = request.POST['last'], email=request.POST['email'], password=hashpass)
            
        return redirect('/')


def main(request):
    context = {
        'user': User.objects.get(id=request.session['logged_in']),
        'books': Book.objects.all(),
        
    }
    return render(request, 'fave_book_app/main.html',context)


def view_edit(request,book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['logged_in'])
    if book.uploader.id != request.session['logged_in']:
        context = {
            'book': book,
            'user': user,
        }
        return render(request, 'fave_book_app/view.html', context)
    else:
        context = {
            'book': book,
            'user': user,
        }
        return render(request, 'fave_book_app/edit.html', context)


def delete(request, book_id):
    delete = Book.objects.get(id=book_id)
    delete.delete()
    return redirect('/main')


def update(request,book_id):
    update = Book.objects.get(id=book_id)
    update.title = request.POST['title']
    update.desc = request.POST['desc']
    update.save()
    return redirect('/main')


def add_fave(request,book_id):
    user = User.objects.get(id=request.session['logged_in'])
    book = Book.objects.get(id=book_id)
    book.liked_users.add(user)
    return redirect('/main')
    



def add(request):

    if request.POST['book'] == 'add':
        print(Book.objects.all().values())
        errors = Book.objects.newBookValidator(request.POST)
        if len(errors) > 0:
            for k,v in errors.items():
                messages.error(request,v)
        else:
            
            user = User.objects.get(id=request.session['logged_in'])
            new_book = Book.objects.create(title = request.POST['title'],
            desc=request.POST['desc'], uploader=user)
        return redirect('/main')


def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('/')


