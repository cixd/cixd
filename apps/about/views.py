from django.shortcuts import render
from apps.about.models import Introduction, Pursuit, Offer

def index(request):
    intro = Introduction.objects.all().order_by('id')
    pursuits = Pursuit.objects.all().order_by('id')
    offer = Offer.objects.all().order_by('id')

    if intro:
        intro = intro[0]
    else:
        intro = ''

    if offer:
        offer = offer[0]
    else:
        offer = ''

    qs = {
        "intro": intro,
        "offer": offer,
        "pursuits": pursuits,
    }

    return render(request, 'about/index.html', qs)
