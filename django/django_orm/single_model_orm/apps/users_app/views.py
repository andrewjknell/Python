from django.shortcuts import render, redirect, HttpResponse
from .models import Users

def index(request):
    context ={
        'all_users': Users.objects.all()
    }
    return render(request,'users_app/index.html', context)
