from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    users = Users.objects.all()
    context = {
        'users': users
    }
    return render(request, "index.html", context)

def create(request):
    if request.method == 'POST':
        newUser = Users.objects.create(
            fname = request.POST['fname'],
            lname= request.POST['fname'],
            email= request.POST['email'],
            age = request.POST['age'],
        )
        newUser.save()
        
    return redirect('/')