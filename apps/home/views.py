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

from .forms import NewSongForm, EditSongForm







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










# def list_songs(request):
#     song_list = Song.objects.all().order_by('id')
#     page_number = request.GET.get('page', 1)
#     paginator = Paginator(song_list, 5)
#     songs = paginator.get_page(page_number)

    
#     if 'HX-Request' in request.headers:
#         return render(request, 'partials/_song_list.html', {'songs': songs})
#     else:
#         return render(request, 'partials/_song_list.html', {'songs': songs})






from django.core.paginator import Paginator
from .models import Song


def list_songs(request):
    # Grab your data, paginate if desired
    
    paginate_number = 10
    
    song_list = Song.objects.all().order_by('id')
    paginator = Paginator(song_list, paginate_number)
    page_number = request.GET.get('page', 1)
    pagination = paginator.get_page(page_number)

    # Check if it's an HTMX request
    if 'HX-Request' in request.headers:
        # Return just the partial
        return render(request, 'partials/_song_list.html', {'pagination': pagination})
    else:
        # Return the main template on a normal GET request
        return render(request, 'home/songs.html', {'songs': pagination})





    

def add_song(request):
    if request.method == "POST":
        form = NewSongForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'songListChanged'})
    else:
        form = NewSongForm()
    return render(request, 'home/new_song_form.html', {
        'form': form,
    })


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Song
from .forms import EditSongForm

def edit_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)

    if request.method == "POST":
        form = EditSongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            # Return 204 so HTMX doesn't replace the modal content;
            # but it triggers "songListChanged" on the client side.
            return render(request, 'home/edit_song_form.html', {
            'form': form,
            'song': song,
        })
        else:
            # If form is invalid, re-render the same partial with errors.
            return render(request, 'home/edit_song_form.html', {
                'form': form,
                'song': song,
            })
    else:
        # GET request: show the form with current song data
        form = EditSongForm(instance=song)
        return render(request, 'home/edit_song_form.html', {
            'form': form,
            'song': song,
        })
