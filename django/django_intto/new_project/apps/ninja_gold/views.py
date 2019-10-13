from django.shortcuts import render, redirect
import random

def show(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, 'ninja_gold/index.html')

def gold(request):
    if request.POST['building'] == 'cave':
        request.session['gold'] = request.session['gold'] + random.randint(5,10)
    if request.POST['building'] == 'farm':
        request.session['gold'] = request.session['gold'] + random.randint(10,20)
    if request.POST['building'] == 'house':
        request.session['gold'] = request.session['gold'] + random.randint(2,5)
    if request.POST['building'] == 'casino':
        request.session['gold'] = request.session['gold'] + random.randint(-50,50)
    return redirect('/ninja_gold')

def reset(request):
    request.session.clear()
    return redirect('/ninja_gold')