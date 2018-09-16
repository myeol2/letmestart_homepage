from django.shortcuts import render

from django.shortcuts import get_object_or_404
from .models import Play
from .models import Gala
# Create your views here.

def index(request):
   
    idx_submenu=1
    play_list = Play.objects.order_by('-idx')
    slides_per_view = 4 
    initial_slide= 0
    context = {
            'play_list': play_list, 
            'idx_submenu': idx_submenu,
            'slides_per_view': slides_per_view,
            'initial_slide': initial_slide,
            }

    return render(request, 'homepage/index.html', context=context)


def team(request):

    type_submenu = 1
    submenu_title = "소개"
    idx_submenu = 2
    context = {
            'type_submenu': type_submenu, 
            'submenu_title': submenu_title,
            'idx_submenu': idx_submenu,
            }

    return render(request, 'homepage/team.html', context=context)

def intro(request):

    type_submenu = 1
    submenu_title = "소개"
    idx_submenu = 1
    context={
            'type_submenu': type_submenu,
            'submenu_title': submenu_title,
            'idx_submenu' : idx_submenu, 
            'id': id,
            }

    return render(request, 'homepage/intro.html', context=context)

def greeting(request):

    type_submenu = 1
    submenu_title = "소개"
    idx_submenu = 3
    id = request.GET.get('id','0')
    context={
            'type_submenu' : type_submenu,
            'submenu_title': submenu_title,
            'idx_submenu': idx_submenu,
            'id': id,
            }
    return render(request, 'homepage/greeting.html', context=context)


def play(request):

    play_list = Play.objects.order_by('-idx')
    type_submenu = 2
    submenu_title="활동"
    idx_submenu = 1
    id = request.GET.get('id', play_list[0].idx)
    play = get_object_or_404(Play, idx=id)
    slides_per_view = 6
    initial_slide = len(play_list)-int(id)
    context={
            'play_list': play_list, 
            'play': play,
            'id': id,
            'type_submenu': type_submenu,
            'submenu_title': submenu_title,
            'idx_submenu' : idx_submenu,
            'slides_per_view': slides_per_view, 
            'initial_slide' : initial_slide,
            }
    return render(request, 'homepage/play.html', context=context)

def gala(request):

    gala_list = Gala.objects.order_by('-idx')
    idx_submenu= 2
    type_submenu= 2 
    submenu_title="활동"
    id = request.GET.get('id',gala_list[0].idx)
    context={
            'type_submenu': type_submenu,
            'idx_submenu': idx_submenu,
            'submenu_title': submenu_title,
            'gala_list': gala_list,
            'id': id,
            }
    return render(request, 'homepage/gala.html', context=context)

def activity(request):

    idx_submenu=3
    type_submenu=2
    submenu_title="활동"
    context={
            'type_submenu': type_submenu,
            'submenu_title': submenu_title,
            'idx_submenu': idx_submenu,
            'id': id,

            }
    return render(request, 'homepage/activity.html', context=context)

def member(request):

    type_submenu = 4;
    play_list = Play.objects.order_by('-idx')
    id = request.GET.get('id', play_list[0].idx)
    play = get_object_or_404(Play, idx=id)
    team_list = play.members.order_by('team').values_list('team', flat=True).distinct()
    
    members_planning = play.members.filter(team__iexact='기획')
    members_stage = play.members.filter(team__iexact='무대')
    members_act = play.members.filter(team__iexact='배우')
    members_stage = play.members.filter(team__iexact='연출')
    members_music = play.members.filter(team__iexact='음악')

    context={
            'play_list': play_list,
            'play': play,
            'team_list': team_list,
            'type_submenu': type_submenu,
            }

    return render(request, 'homepage/member.html', context=context)

def faq(request):
    
    type_submenu = 4;
    idx_submenu=2

    context ={
            'idx_submenu':idx_submenu,
            'type_submenu': type_submenu,
            }
    return render(request, 'homepage/FAQ.html', context=context)

def recruit(request):
    type_submenu = 4;
    idx_submenu=1
    context= {
            'idx_submenu': idx_submenu,
            'type_submenu': type_submenu,
            }
    
    return render(request, 'homepage/recruit.html', context=context)

def contact(request):

    return render(request, 'homepage/contact.html')


