from django import template

def embed(value):
    link = "http://www.youtube.com/embed/" + value.split("/")[-1]

    return link

register = template.Library()
register.filter('embed', embed)
