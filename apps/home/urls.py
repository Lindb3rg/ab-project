# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('add_song/', views.add_song, name='add_song'),
    path('edit-song/<int:song_id>/', views.edit_song, name='edit_song'),
    path('list_songs/', views.list_songs, name='list_songs'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
