from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from datetime import datetime
import bcrypt

def index(request):
    return render(request, 'index.html')

def create_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode()
        user=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password= password)
        request.session['uid']= user.id
        return redirect('/dashboard')
    
    
    
        
def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if len(user) > 0:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['uid'] = logged_user.id
            return redirect('/dashboard')
        else:
            messages.error(request, 'Email and password did not match')
            
    else:
        messages.error(request, 'Email is not registered')
    return redirect('/')


# dashboard method
def dashboard(request):
    if 'uid' not in request.session:
        return redirect('/')
    else:
        context = {
            'logged_user': User.objects.get(id=request.session['uid']),
            'all_wishes': Wish.objects.filter(grant_wish=0),
            'granted_wishes': Wish.objects.filter(grant_wish=1),
        }

        return render(request, 'dashboard.html', context)
    
    
    
# make a wish
def new_wish(request):
    if 'uid' not in request.session:
        return redirect('/')
    else:
        context = {
            'logged_user': User.objects.get(id=request.session['uid']),
        }
        return render(request, 'new_wish.html', context)


def create_wish(request):
    errors = Wish.objects.wish_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/wishes/new')
    else:
        new_wish = Wish.objects.create(title= request.POST['title'], desc = request.POST['desc'],poster = User.objects.get(id=request.session['uid']))
        return redirect('/dashboard')

    return redirect('/wishes/new')


# edit wish
def edit_wish(request, id):
    if 'uid' not in request.session:
        return redirect('/')
    else:
        context={
            'edit_wish': Wish.objects.get(id=id),
        }
        
        return render(request, 'edit.html', context)


# update wish
def update(request, id):
    if 'uid' not in request.session:
        return redirect('/')
    else:
        errors = Wish.objects.wish_validator(request.POST)
        if len(errors) > 0:
            str_id=str(id)
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/wishes/edit/{str_id}')
        else:
            str_id=str(id)
            edit_wish=Wish.objects.get(id=id)
            edit_wish.title=request.POST['title']
            edit_wish.desc=request.POST['desc']
            edit_wish.save()
        
        return redirect('/dashboard')
        

#delete wish
def destroy(request, id):
    if 'uid' not in request.session:
        return redirect('/')
    else:
        Wish.objects.get(id=id).delete()
        return redirect('/dashboard')
    
# granted wishes
def grant(request, wish_id):
    if 'uid' not in request.session:
        return redirect('/')
    else:
        wish = Wish.objects.get(id=wish_id)
        wish.grant_created = datetime.now()
        wish.grant_wish = 1
        wish.save()       
        
        return redirect('/dashboard')
    

        
    
# like a wish
def like_wish(request, wish_id):
    if 'uid' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['uid'])
        wish = Wish.objects.get(id=wish_id)
        
        user.liked_wishes.add(wish)
        
        return redirect('/dashboard')


# delete like
def delete_like(request, wish_id):
    if 'uid' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['uid'])
        wish =Wish.objects.get(id=wish_id)
        
        user.liked_wishes.remove(wish)
        
        return redirect('/dashboard')

def stats(request):
    if 'uid' not in request.session:
        return redirect('/')
    else:
        user=User.objects.get(id=request.session['uid'])
        context={
            'granted_wishes': Wish.objects.filter(grant_wish=1).count(),
            'my_granted_wishes': Wish.objects.filter(grant_wish=1, poster=user).count(),
            'my_pending_wishes': Wish.objects.filter(grant_wish=0, poster=user).count(),
            'logged_user': User.objects.get(id=request.session['uid'])
                      
        }
        
        return render(request, 'stats.html', context)
    
# log out 
def log_out(request):
    request.session.clear()
    return redirect('/')