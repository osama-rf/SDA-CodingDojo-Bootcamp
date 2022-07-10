from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            request.session['user_id'] = User.objects.get(email=request.POST['email']).id
            return redirect('/success')

def register(request):
    if request.method == 'POST':
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            newUser = User.objects.create(
                name = request.POST['name'],
                email = request.POST['email'],
                password = hash
            )
            newUser.save()
            request.session['user_id'] = newUser.id
            return redirect('/success')

def signout(request):
    del request.session['user_id']
    return redirect("/")

def success(request):
    if not 'user_id' in request.session:
        return redirect('')
    context = {
        "user" : User.objects.get(id=request.session['user_id']),
        "movies" : Movie.objects.all()
    }
    return render(request, "success.html", context)

def user_profile(request):
    if not 'user_id' in request.session:
        return redirect('')
    context = {
        "user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'profile.html', context)

def add(request, id):
    movie = Movie.objects.get(id=id)
    user = User.objects.get(id=request.session['user_id'])
    user.lists.add(movie)
    # movie.users_list.add(movie)
    return redirect('/user_profile')

def movie_profile(request, id):
    if not 'user_id' in request.session:
        return redirect('')
    context = {
        "movie": Movie.objects.get(id=id)
    }
    return render(request, 'movie_profile.html', context)

def like(request,id):
    movie = Movie.objects.get(id=id)
    user = User.objects.get(id=request.session['user_id'])
    user.likes.add(movie)
    # movie.users_list.add(movie)
    return redirect(f'/movie_profile/{id}')

def dislike(request,id):
    movie = Movie.objects.get(id=id)
    user = User.objects.get(id=request.session['user_id'])
    user.likes.remove(movie)
    # movie.users_list.add(movie)
    return redirect(f'/movie_profile/{id}')
