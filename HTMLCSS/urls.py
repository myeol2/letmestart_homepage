from django.urls import path

from . import views

urlpatterns = [
        path('index', views.index, name='index'),
        path('activity', views.activity, name='activity'),
        path('recruit', views.recruit, name='recruit'),
        path('contact', views.contact, name='contact'),
        path('play', views.play, name='play'),        
        path('intro/introduction', views.intro, name= 'intro'),
        path('intro/team', views.team, name='team'),
        ]

