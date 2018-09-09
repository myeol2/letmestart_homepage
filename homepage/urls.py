from django.urls import path

from . import views

urlpatterns = [
        path('', views.index),
        path('index', views.index, name='index'),
        path('activity', views.activity, name='activity'),
        path('recruit', views.recruit, name='recruit'),
        path('contact', views.contact, name='contact'),
        path('intro', views.intro, name= 'intro'),
        path('intro/team', views.team, name='team'),
        path('intro/greeting', views.greeting, name="greeting"),
        path('play', views.play, name="play"),
        path('gala', views.gala, name="gala"),
        path('activity', views.activity, name="activity"),
        path('member', views.member, name="member"),
        ]

