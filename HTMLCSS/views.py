from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'HTMLCSS/index.html')

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
