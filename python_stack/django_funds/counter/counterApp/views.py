from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    
    return render(request, "index.html")


def destroy(request):
    del request.session['counter']
    return redirect('/')

