from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method == 'POST':
        errors = Users.objects.registar_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            hash_pass = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode()
            user = Users.objects.create(
                fname = request.POST['fname'],
                lname = request.POST['lname'],
                email = request.POST['email'],
                password = hash_pass
            )
            user.save()
            messages.success(request,"User successfuly added")

            request.session['user_id'] = user.id

    return redirect('/')

def welcome(request):
    context = {
        'user' : Users.objects.get(id = request.session['user_id'])
    }

    return render(request, "success.html", context)


def login(request):
    if request.method == 'POST':
        errors = Users.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            userid = Users.objects.get(email__iexact=request.POST['email'])
            request.session['user_id'] = userid.id
            return redirect('/success')
    return redirect('/')

def logout(request):
    del request.session['user_id']
    return redirect('/')

# def logout(request):
#     del request.session.clear()