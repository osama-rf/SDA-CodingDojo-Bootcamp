from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# def index(request):
#     return HttpResponse("response from index method from root route, localhost:8000!")
    
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)

