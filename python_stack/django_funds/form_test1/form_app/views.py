from django.shortcuts import render, redirect, HttpResponse

def index(request):
    # this is the route that shows the form
    return render(request,"index.html")
def create_user(request):
    # this is the route that processes the form
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    context = {
        "name_on_template" : name_from_form,
        "email_on_template" : email_from_form
    }
    return redirect("/success")
def success(request):
    # this is the success route
    return render(request, "success.html")