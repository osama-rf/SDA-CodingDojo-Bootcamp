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

    _user = User.objects.get(id = request.session['user_id'])
    context = {
        'user': _user,
        'your_job': Job.objects.filter(user=_user , done=False),
        'other_jobs': Job.objects.all()
    }
    return render(request, 'dashboard.html', context)


def logout(request):
    if 'user_id' not in request.session:
        return redirect('/')

    del request.session['user_id']
    return redirect('/')


def new_job(request):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, ('new_job.html', context))

def create_job(request):
    if 'user_id' not in request.session:
        return redirect('/')

    if request.method == 'POST':
        errors = Job.objects.job_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value) 
        else:
            _user = User.objects.get(id= request.session['user_id'])
            make_job = Job.objects.create(
                job = request.POST['job'],
                desc = request.POST['desc'],
                loc = request.POST['loc'],
                user = _user
            )
            make_job.save()
            messages.success(request, "Job added successfully!")
            return redirect('/dashboard')
    return redirect('/jobs/new')

def view_job(request, job_id):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'job':Job.objects.get(id=job_id),
        'user': User.objects.get(id=request.session['user_id']),
    }

    return render(request,'view_job.html',context)

def add_job(request, job_id):
    if 'user_id' not in request.session:
        return redirect('/')

    return redirect ('/dashboard')

def edit_job(request, job_id):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'job': Job.objects.get(id= job_id),
    }
    return render(request, 'edit.html', context)

def update_job(request, job_id):
    if 'user_id' not in request.session:
        return redirect('/')

    if request.method == 'POST':
        errors = Job.objects.job_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
        else:
            make_job = Job.objects.get(id=job_id)
            make_job.job = request.POST['job']
            make_job.desc = request.POST['desc']
            make_job.loc = request.POST['loc']
            make_job.save()
            messages.success(request, "Job updated successfully!")
            return redirect('/dashboard')
        return redirect(f'/jobs/{job_id}/edit')

def delete(request, job_id):
    _job= Job.objects.get(id=job_id)
    _job.delete()

    return redirect('/dashboard')