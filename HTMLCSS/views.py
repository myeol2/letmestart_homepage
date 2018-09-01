from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'HTMLCSS/index.html')

def team(request):

    return render(request, 'HTMLCSS/team.html')




