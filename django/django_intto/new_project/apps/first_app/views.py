from django.shortcuts import render, HttpResponse, redirect



def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "first_app/index.html", context)
  

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    return redirect('/')

def show(request, my_val):
    return HttpResponse(f'placeholder to display blog number {my_val}')

def edit(request, val):
    return HttpResponse(f'placeholder to edit blog {val}')

def destroy(request, val):
    return redirect('/')