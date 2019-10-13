from django.shortcuts import render
from time import gmtime, strftime


from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'time_app/index.html',context)

def time(request):
    context = {
        'time': strftime("%B %d, %Y %H:%M:%S")
    }
    return render(request,'time_app/index.html',context)