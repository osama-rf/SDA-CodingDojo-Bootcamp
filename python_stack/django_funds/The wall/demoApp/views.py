from contextlib import redirect_stderr
import bcrypt
from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse
from .models import *

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        errors = Users.objects.validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            pwHash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            newUser = Users.objects.create(fname=fname,lname=lname,email=email,password=pwHash)
            newUser.save()
            request.session['loggedInUser'] = newUser.id
            return redirect('/home')

def login(request):
    if request.method=='POST':
        users = Users.objects.filter(email=request.POST['email'])
        if len(users)==1:
            if not bcrypt.checkpw(request.POST['password'].encode(),users[0].password.encode()):
                messages.error(request, "Email or Password is incorrect!")
                return redirect('/')
            else:
                request.session['loggedInUser'] = users[0].id
                return redirect('/home')
        else:
            messages.error(request, "Email does not exist!")
            return redirect('/')
            

def home(request):
    if not 'loggedInUser' in request.session:
        return redirect('/')
    else:
        context = {
            'user':Users.objects.get(id=request.session['loggedInUser']),
            'posts':Users.objects.get(id=request.session['loggedInUser']).posts.order_by('-createdAt')
        }
        return render(request,'profilePage.html',context)

def logout(request):
    request.session.clear()
    return redirect('/')

def createPost(request):
    if request.method == 'POST':
        errors = Posts.objects.validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/home')
        else:
            title = request.POST['title']
            content = request.POST['content']
            user = Users.objects.get(id=request.session['loggedInUser'])
            newPost = Posts.objects.create(title=title,content=content,user=user)
            newPost.save()
            return redirect('/home')

def feed(request):
    context={
        'posts':Posts.objects.all().order_by('-createdAt')
    }
    return render(request,'feed.html',context)

def other(request,id):
    request.session['otherUser'] = id
    return redirect('/otherHome')

def otherHome(request):
    context={
        'user':Users.objects.get(id=request.session['otherUser']),
        'posts':Users.objects.get(id=request.session['otherUser']).posts.order_by('-createdAt')
    }
    return render(request,'profilePage.html',context)