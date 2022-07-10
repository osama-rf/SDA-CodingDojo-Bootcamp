from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Users
import bcrypt


# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    return redirect('/success')

def success(request):
    return render(request, "success.html")
    
