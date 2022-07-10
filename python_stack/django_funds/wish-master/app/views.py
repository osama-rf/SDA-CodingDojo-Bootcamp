from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        errors = User.objects.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            hash_pass = bcrypt.hashpw(
                request.POST['password'].encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=hash_pass
            )
            user.save()
            messages.success(request, "User successfully added!")

            request.session['user_id'] = user.id
            return redirect('/wishes')
    return redirect('/')


def login(request):
    if request.method == 'POST':
        errors = User.objects.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            userid = User.objects.get(email__iexact=request.POST['email'])
            request.session['user_id'] = userid.id
            return redirect('/wishes')

    return redirect('/')


def wishes(request):
    active_session = request.session.get("user_id")
    if active_session:
        user = User.objects.filter(id=active_session).first()
        granted_wishes = Wish.objects.filter(
            granted=True).order_by("-created_at")
        pending_wishes = Wish.objects.filter(
            granted=False, user=user).order_by("-created_at")
        likes = Like.objects.all()
        context = {
            "user": user,
            "granted_wishes": granted_wishes,
            "pending_wishes": pending_wishes,
            "likes": likes,
        }
        return render(request, "wishes.html", context)
    else:
        return redirect("/")


def logout(request):
    request.session.clear()
    return redirect("/")


def create_wish(request):
    errors = Wish.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/wishes/new")
    else:
        Wish.objects.create(
            item=request.POST["item"],
            description=request.POST["description"],
            granted=False,
            user=User.objects.get(id=request.session.get("user_id"))
        )
        return redirect("/wishes")


def new_wish(request):
    return render(request, "new_wish.html")


def delete_wish(request, id):
    wish = Wish.objects.filter(id=id).first()
    wish.delete()
    return redirect("/wishes")


def edit_wish(request, id):
    this_wish = Wish.objects.filter(id=id).first()
    context = {
        "wish": this_wish
    }
    return render(request, "edit_wish.html", context)


def update_wish(request):
    errors = Wish.objects.validator(request.POST)
    # make sure to pass in ID to this function in the edit_wish html as hidden input
    edit_id = request.POST["id"]
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # might need to remove leading slash from redirect
        return redirect(f"/wishes/edit/{edit_id}")
    else:
        wish_to_edit = Wish.objects.filter(id=edit_id).first()
        wish_to_edit.item = request.POST["item"]
        wish_to_edit.description = request.POST["description"]
        wish_to_edit.save()
        # might need to remove leading slash from redirect
        return redirect("/wishes")


def grant_wish(request, id):
    granting = Wish.objects.filter(id=id).first()
    granting.granted = True
    granting.save()
    return redirect("/wishes")


def stats(request):
    user = User.objects.get(id=request.session.get("user_id"))
    total_granted_wishes = Wish.objects.filter(granted=True)
    user_granted_wishes = total_granted_wishes.filter(
        user=user)
    user_pending_wishes = Wish.objects.filter(
        user=user, granted=False)
    context = {
        "total_granted_wishes": total_granted_wishes,
        "user_granted_wishes": user_granted_wishes,
        "user_pending_wishes": user_pending_wishes
    }
    return render(request, 'stats.html', context)


def like(request, id):
    wish = Wish.objects.filter(id=id).first()
    user = User.objects.get(id=request.session["user_id"])
    like = Like.objects.filter(
        user=user, wish=wish
    ).first()
    if like:
        like.delete()
    else:
        newLike = Like.objects.create(
            liked=True, user=user, wish=wish
        )
    return redirect("/wishes")
