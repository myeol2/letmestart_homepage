from django.urls import path

from . import views

urlpatterns = [
        path('index', views.index, name='index'),
        path('team', views.team, name='team'),
        path('activity', views.activity, name='activity'),
        path('recruit', views.recruit, name='recruit'),
        path('contact', views.contact, name='contact'),
        path('play', views.play, name='play'),        
        ]

