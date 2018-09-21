from django import template
from django.db.models import Max

register = template.Library()

@register.filter
def in_team(things, team):
    return things.filter(team=team)

@register.filter
def index(List, i):
    return List[int(i)]

@register.filter
def distinct(things, field):
	return things.values(field).distinct()

@register.filter
def distinct_member(things):
    return things.values('admission_order_letme', 'name', 'admission_year', 'major').order_by().annotate(position=Max('position')).order_by('-position')






















