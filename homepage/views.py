from django.shortcuts import render
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from .models import Play
from .models import PlayMember
from .models import Gala
from .models import Etc
# Create your views here.

chiefs = Etc.objects.all().order_by('-idx')[0].chiefs.all() 

def index(request):
   
    idx_submenu=1
    play_list = Play.objects.order_by('-idx')
    recent_play = play_list[0]
    slides_per_view = 4 
    initial_slide= 0

    context = {
            'play_list': play_list, 
            'idx_submenu': idx_submenu,
            'slides_per_view': slides_per_view,
            'initial_slide': initial_slide,
            'chiefs' : chiefs,            
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
            'chiefs' : chiefs,            
            }

    return render(request, 'homepage/team.html', context=context)

def intro(request):

    type_submenu = 1
    submenu_title = "소개"
    idx_submenu = 1
    
    recent_play = Play.objects.all().order_by('-idx')[0]
    num_of_members = len(PlayMember.objects.all().values('admission_order_letme', 'admission_year', 'name').distinct())
    num_of_audiences = Play.objects.values().aggregate(total_price=Sum('num_of_audience'))['total_price']
    context={
            'type_submenu': type_submenu,
            'submenu_title': submenu_title,
            'idx_submenu' : idx_submenu, 
            'id': id,
            'recent_play' : recent_play,
            'num_of_members' : num_of_members,
            'num_of_audiences' : num_of_audiences,
            'chiefs' : chiefs,            
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
            'chiefs' : chiefs,            
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
            'chiefs' : chiefs,            
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
            'chiefs' : chiefs,            
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
            'chiefs' : chiefs,            

            }
    return render(request, 'homepage/activity.html', context=context)

def member(request):

    type_submenu = 3;
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
            'chiefs' : chiefs,            
            }

    return render(request, 'homepage/member.html', context=context)

def faq(request):
    
    type_submenu = 4;
    idx_submenu=2

    context ={
            'idx_submenu':idx_submenu,
            'type_submenu': type_submenu,
            'chiefs' : chiefs,            
            }
    return render(request, 'homepage/FAQ.html', context=context)

def recruit(request):
    type_submenu = 4;
    idx_submenu=1
    context= {
            'idx_submenu': idx_submenu,
            'type_submenu': type_submenu,
            'chiefs' : chiefs,            
            }
    
    return render(request, 'homepage/recruit.html', context=context)

def contact(request):

    return render(request, 'homepage/contact.html')


