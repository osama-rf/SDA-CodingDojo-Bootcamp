from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def index(request):
    return redirect('/shows')


def show_new(request):
    return render(request, 'new_show.html')


def create_show(request):
    if request.method == 'POST':
        errors = Show.objects.showValidator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            show = Show.objects.create(
                title=request.POST['title'],
                network=request.POST['network'],
                release_date=request.POST['release_date'],
                description=request.POST['description']
            )
            show.save()
            return redirect(f'/shows/{show.id}')

    return redirect('/shows/new')


def show(request, show_id):
    _show = Show.objects.get(id=show_id)
    context = {
        'show': _show
    }

    return render(request, 'read_show.html', context)


def all_shows(request):
    _shows = Show.objects.all()
    context = {
        'shows': _shows
    }
    return render(request, 'all_shows.html', context)


def show_edit(request, show_id):
    _show = Show.objects.get(id=show_id)
    context = {
        'show': _show
    }
    return render(request, 'edit_show.html', context)


def update_show(request, show_id):
    if request.method == 'POST':
        errors = Show.objects.updateValidator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            _show = Show.objects.get(id=show_id)
            _show.title = request.POST['title']
            _show.network = request.POST['network']
            _show.description = request.POST['description']
            _show.release_date = request.POST['release_date']

            _show.save()
            return redirect(f'/shows/{_show.id}')

        return redirect(f'/shows/{_show.id}/edit')


def show_destroy(request, show_id):
    if request.method == 'POST':
        _show = Show.objects.get(id=show_id)
        _show.delete()

    return redirect('/shows')
