from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def add_show(request):
    errors = Show.objects.basic_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/add')
    else:
        new_show = Show.objects.create(title=request.POST['title'],
        network=request.POST['network'],release_date=request.POST['release'],
        description=request.POST['desc'])
        show_id = new_show.id
    return redirect('/{}'.format(show_id))


def view_add_page(request):
    return render(request, 'tv_app/add_show.html')


def view_all(request):
    context = {
        'shows': Show.objects.all(),
        
    }
    return render(request, 'tv_app/view_all.html',context)


def page_edit_show(request, get_id):
    context = {
        'show': Show.objects.get(id=get_id)
    }

    return render(request, 'tv_app/edit_show.html',context)


def edit_show(request, get_id):
    errors = Show.objects.basic_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/'+get_id +'/edit')
    else:
        update_show = Show.objects.get(id=get_id)
        update_show.title=request.POST['title']
        update_show.network=request.POST['network']
        update_show.release_date=request.POST['release']
        update_show.description=request.POST['desc']
        update_show.save()
    return redirect('/'+ get_id)


def view_show(request, get_id):
    context = {
       'show': Show.objects.get(id=get_id)
    }
    return render(request, 'tv_app/view_show.html', context)


def delete_show(request, get_id):
    delete = Show.objects.get(id=get_id)
    delete.delete()
    return redirect('/view')

