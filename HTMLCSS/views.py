from django.shortcuts import render

# Create your views here.

def index(request):
    play_index =  [2,3,4,5,7,8,9,10,11,12,13,14,15]
    
    context = {'idx_play': reversed(play_index)}

    return render(request, 'HTMLCSS/index.html', context)

def activity(request):

    return render(request, 'HTMLCSS/activity.html')


def team(request):

    return render(request, 'HTMLCSS/team.html')

def recruit(request):

    return render(request, 'HTMLCSS/recruit.html')

def contact(request):

    return render(request, 'HTMLCSS/contact.html')

def play(request):

    return render(request, 'HTMLCSS/play.html')

def intro(request):
    
    return render(request, 'HTMLCSS/intro.html')
