from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        errors = User.objects.register_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            hash_pass = bcrypt.hashpw(
                request.POST['password'].encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(
                fname=request.POST['fname'],
                lname=request.POST['lname'],
                email=request.POST['email'],
                password=hash_pass
            )
            user.save()
            messages.success(request, "User successfully added!")

            request.session['user_id'] = user.id
            return redirect('/dashboard')
    return redirect('/')


def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            userid = User.objects.get(email__iexact=request.POST['email'])
            request.session['user_id'] = userid.id
            return redirect('/dashboard')

    return redirect('/')


def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')

    _user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': _user,
        'your_wish': Wish.objects.filter(user=_user , done=False).order_by("created_at"),
        'granted_wish': Granted.objects.filter(wish__done=True).order_by("created_at"),
    }
    return render(request, 'dashboard.html', context)


def logout(request):
    if 'user_id' not in request.session:
        return redirect('/')

    del request.session['user_id']
    return redirect('/')

def new_wish(request):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'user': User.objects.get(id = request.session['user_id'])
    }
    return render(request, ('create_wish.html', context))


def create_wish(request):
    if 'user_id' not in request.session:
        return redirect('/')

    if request.method == 'POST':
        errors = Wish.objects.wish_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value) 
        else:
            _user = User.objects.get(id= request.session['user_id'])
            make_wish = Wish.objects.create(
                wish = request.POST['wish'],
                desc = request.POST['desc'],
                user = _user
            )

            make_wish.save()
            messages.success(request, "wish added successfully!")
            return redirect('/dashboard')
    return redirect('/wish/new')

def edit_wish(request, wish_id):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'wish': Wish.objects.get(id= wish_id),
    }
    return render(request, 'edit_wish.html', context)


def grant(request, wish_id):
    if 'user_id' not in request.session:
        return redirect('/')

    _wish = Wish.objects.get(id = wish_id)
    _wish.done = True
    _wish.save()
    grant = Granted.objects.create(
        wish = _wish
    )

    grant.save()

    return redirect ('/dashboard')

def update_wish(request,wish_id):
    if 'user_id' not in request.session:
        return redirect('/')

    if request.method == 'POST':
        errors = Wish.objects.wish_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
        else:
            make_wish = Wish.objects.get(id=wish_id)
            make_wish.wish = request.POST['wish']
            make_wish.desc = request.POST['desc']
            make_wish.save()
            messages.success(request, "wish updated successfully!")
            return redirect('/dashboard')
        return redirect(f'/wish/{wish_id}/edit')



def likes(request, granted_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        _like = Granted.objects.get(id= granted_id)
        _user = User.objects.get(id= request.session['user_id'])
        _like.like.add(_user)
        _like.save()
    return redirect('/dashboard')

def delete(request, wish_id):

    _wish= Wish.objects.get(id=wish_id)
    _wish.delete()

    return redirect('/dashboard')


def state(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id = request.session['user_id']),
            'granted_wish': Granted.objects.all(),
        }
        return render(request, 'state.html', context)

