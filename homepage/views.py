from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Play

# Create your views here.

def index(request):
    
    play_list = Play.objects.order_by('-idx')
    slides_per_view = 4 
    context = {
            'play_list': play_list, 
            'idx_submenu': 1,
            'slides_per_view': slides_per_view,
            }

    return render(request, 'homepage/index.html', context=context)


def team(request):
    
    type_submenu = "intro"
    idx_submenu = 1
    context = {
            'type_submenu': type_submenu, 
            'idx_submenu': idx_submenu,
            }

    return render(request, 'homepage/team.html', context=context)

def recruit(request):

    return render(request, 'homepage/recruit.html')

def contact(request):

    return render(request, 'homepage/contact.html')


def intro(request):
    
    type_submenu = 'intro'
    idx_submenu = 2
    context={
            'type_submenu': type_submenu,
            'idx_submenu' : idx_submenu, 
            'id': id,
            }

    return render(request, 'homepage/intro.html', context=context)

def greeting(request):
    type_submenu = 'intro'
    id = request.GET.get('id','0')
    context={
            'type_submenu' : type_submenu,
            'idx_submenu': 3,
            'id': id,
            }
    return render(request, 'homepage/greeting.html', context=context)


def play(request):
 
    play_list = Play.objects.order_by('-idx')
    type_submenu = 'activity'
    id = request.GET.get('id', len(play_list))
    play = get_object_or_404(Play, idx=id)
    slides_per_view = 6
    
    context={
            'play_list': play_list, 
            'play': play,
            'id': id,
            'type_submenu': type_submenu,
            'slides_per_view': slides_per_view, 
            }
    return render(request, 'homepage/play.html', context=context)

def gala(request):
    
    type_submenu = 'activity'
    id = request.GET.get('id','0')
    context={
            'type_submenu': type_submenu,
            'id': id,
            }
    return render(request, 'homepage/gala.html', context=context)

def activity(request):
    
    type_submenu = 'activity'
    context={
            'type_submenu': type_submenu,
            'id': id,
            }
    return render(request, 'homepage/activity.html', context=context)

