from django.shortcuts import render

# Create your views here.

def index(request):
    play_index = list(range(1,16))
    slides_per_view = 4 
    context = {
            'idx_play': reversed(play_index),
            'idx_submenu': 1,
            'slides_per_view': slides_per_view,
            }

    return render(request, 'homepage/index.html', context=context)


def team(request):
    
    type_submenu = "intro"
    context = {
            'type-submenu': 'intro', 
            }

    return render(request, 'homepage/team.html', context=context)

def recruit(request):

    return render(request, 'homepage/recruit.html')

def contact(request):

    return render(request, 'homepage/contact.html')


def intro(request):
    
    type_submenu = 'intro'
    context={
            'type_submenu': type_submenu,
            'id': id,
            }

    return render(request, 'homepage/intro.html', context=context)

def greeting(request):
    type_submenu = 'intro'
    
    id = request.GET.get('id','0')
    context={
            'idx_submenu': idx_submenu,
            'id': id,
            }
    return render(request, 'homepage/greeting.html', context=context)


def play(request):
   
    play_index = list(range(1,16))
    type_submenu = 'activity'
    id = request.GET.get('id','0')
    slides_per_view = 6
    context={
            'idx_play': reversed(play_index),
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

