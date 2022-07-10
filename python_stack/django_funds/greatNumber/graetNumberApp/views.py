from django.shortcuts import render, HttpResponse, redirect
import random


def index(request):
    if "guess" not in request.session:
        request.session['guess'] = random.randint(1, 100)
    return render(request, "index.html")


def guess(request):
    isTrue = "not setted"
    color = "regular"
    message = "nothing for now"
    if int(request.POST['rndm']) == request.session['guess']:
        isTrue = True
        color = "green"
        message = f"{request.session['guess']} is the number I choice"
    elif int(request.POST['rndm']) > request.session['guess']:
        isTrue = False
        color = "red"
        message = "Too High!"
    else:
        isTrue = False
        color = "red"
        message = "Too low!"

    context = {
        'rndm': isTrue,
        'color': color,
        'message': message,
    }
    return render(request, "index.html", context)


def destroy(request):
    del request.session['guess']
    return redirect('/')
