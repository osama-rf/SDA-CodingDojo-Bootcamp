from django.shortcuts import render, redirect
from .models import User, Wish, Wish_granted
from django.contrib import messages
import bcrypt
from datetime import date

def index(request):
    if 'uid' in request.session:
        return redirect("/wishes")
    context = {
        'today': date.today()
    }
    return render(request, "index.html", context)

def register(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        password = request.POST['password']
        pwd_hash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()
        print(pwd_hash)
        new_user = User.objects.create(
            fname=request.POST['fname'],
            lname=request.POST['lname'],
            email=request.POST['email'],
            password=pwd_hash)
        request.session['uid'] = new_user.id
        return redirect("/wishes")

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        logged_user = User.objects.get(email=request.POST['email'])
        request.session['uid'] = logged_user.id
        return redirect('/wishes')
    return redirect("/")

def wishes(request):
    if 'uid' not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['uid']),
        "wishes": User.objects.get(id=request.session['uid']).wishes.all(),
        "wishes_granted": Wish_granted.objects.all()
    }
    return render(request, "wishes.html", context)

def new(request):
    if 'uid' not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['uid'])
    }
    return render(request, "new.html", context)

def create(request):
    if request.method == "POST":
        errors = Wish.objects.wish_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/wishes/new")
        Wish.objects.create(
            theWish=request.POST['theWish'],
            desc=request.POST['desc'],
            user=User.objects.get(id=request.session['uid'])
        )
    return redirect("/wishes")

def delete(request, wish_id):
    this_wish = Wish.objects.get(id=wish_id)
    this_wish.delete()
    return redirect("/wishes")

def update(request, wish_id):
    if request.method == "POST":
        errors = Wish.objects.wish_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/edit")
        this_wish = Wish.objects.get(id=wish_id)
        this_wish.theWish = request.POST['theWish']
        this_wish.desc = request.POST['desc']
        this_wish.save()
    return redirect("/wishes")

def grant(request, wish_id):
    if request.method == 'POST':
        Wish_granted.objects.create(theWish=request.POST['theWish'], user=User.objects.get(id=request.POST['uid']))
        wish = Wish.objects.get(id=request.POST['wish_id'])
        wish.delete()
    return redirect('/wishes')

def edit(request, wish_id):
    context = {
        "user": User.objects.get(id=request.session['uid']),
        "wish": Wish.objects.get(id=wish_id)
    }
    return render(request, "edit.html", context)

# def like(request):
#     if request.method == 'POST':
#         wish_granted = Wish_granted.objects.get(id=request.POST['grant_id'])
#         user = User.objects.get(id=request.POST['uid'])
#         if wish_granted.uid == user.id:
#             messages.error(request, "can not like your wish")
#             return redirect('/wishes')
#         if len(wish_granted.likes.filter(id=request.POST['uid'])) > 0:
#             messages.error(request, "You already liked this wish")
#             return redirect('/wishes')
#         else:
#             wish_granted.likes.add(user)
#             return redirect('/wishes')
        
def logout(request):
    request.session.flush()
    return redirect("/")

