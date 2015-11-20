from django import template

def embed(value):
    link = "http://www.youtube.com/embed/" + value.split("/")[-1]

    return link

def recent(value):
    topics = value[:3]

    return topics

def more(value):
    topics = value[3:]

    return topics

register = template.Library()
register.filter('embed', embed)
register.filter('recent', recent)
register.filter('more', more)
