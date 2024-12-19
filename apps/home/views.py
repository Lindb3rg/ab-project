# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render

from . import models





# @login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        
        
        
        
        return HttpResponse(html_template.render(context, request))
        
        

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def transactions(request):
    context = {'segment': 'transactions'}

    html_template = loader.get_template('home/transactions.html')
    return HttpResponse(html_template.render(context, request))

from .forms import SongForm


def add_song_original(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204)  # You can also redirect here, depending on your use case
    else:
        form = SongForm()

    return render(request, 'home/song_form.html', {
        'form': form,
    })


from .models import Song  

def list_songs(request):
    songs = Song.objects.all()
    return render(request, 'home/list_songs.html', {'songs': songs})
        

    

def add_song(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'songListChanged'})
    else:
        form = SongForm()
    return render(request, 'home/song_form.html', {
        'form': form,
    })

