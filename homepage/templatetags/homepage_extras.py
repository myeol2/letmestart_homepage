from django import template

register = template.Library()

@register.filter
def in_team(things, team):
    return things.filter(team=team)



























