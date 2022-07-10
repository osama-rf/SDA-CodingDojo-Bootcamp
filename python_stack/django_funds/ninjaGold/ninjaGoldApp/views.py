from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0

    if 'log' not in request.session:
        request.session['log'] = []

    if request.method == "POST":
        if request.POST['location'] == "farm" or request.POST['location'] == "cave" or request.POST['location'] == "house":
            num = random.randint(10, 20)
            request.session['log'].append(
                f"You entered a {request.POST['location']} and earned {num} gold.")

            request.session["gold"] += num
        else:
            num = random.randint(-50, 50)
            if num > -1:
                request.session['log'].append(
                    f"You earned a {request.POST['location']} and earned {num} of gold.")
            else:
                request.session['log'].append(f"You failed a {request.POST['location']} and lost{num} gold. Ouch")

            request.session['gold'] += num

    return render(request, "index.html")


def destroy(request):
    del request.session['color']
    del request.session['log']
    del request.session['gold']
    return redirect('/')
