from django.shortcuts import render

# Create your views here.

def index(request):
    play_index =  [2,3,4,5,7,8,9,10,11,12,13,14,15]
     
    context = {
            'idx_play': reversed(play_index),
            'idx_submenu': 1,
            }

    return render(request, 'HTMLCSS/index.html', context)

def activity(request):

    return render(request, 'HTMLCSS/activity.html')


def team(request):
    
    context = {
            'idx_submenu': 2, 
            }

    return render(request, 'HTMLCSS/team.html', context=context)

def recruit(request):

    return render(request, 'HTMLCSS/recruit.html')

def contact(request):

    return render(request, 'HTMLCSS/contact.html')


def intro(request):
    
    return render(request, 'HTMLCSS/intro.html')

def greeting(request):
    
    id = request.GET.get('id','0')
    context={
            'id': id,
            }
    return render(request, 'HTMLCSS/greeting.html', context)


def play(request):
    
    id = request.GET.get('id','0')
    context={
            'id': id,
            }
    return render(request, 'HTMLCSS/play.html', context)

def gala(request):
    
    id = request.GET.get('id','0')
    context={
            'id': id,
            }
    return render(request, 'HTMLCSS/gala.html', context)

def activity(request):
    
    context={
            'id': id,
            }
    return render(request, 'HTMLCSS/activity.html', context)

