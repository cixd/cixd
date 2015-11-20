from django.shortcuts import render
from apps.about.models import Introduction, Pursuit, Offer, Contact

def index(request):
    intro = Introduction.objects.all().order_by('id')
    pursuits = Pursuit.objects.all().order_by('id')
    offer = Offer.objects.all().order_by('id')
    contact = Contact.objects.all().order_by('id')

    if intro:
        intro = intro[0]
    else:
        intro = ''

    if not pursuits:
        pursuits = ''


    if offer:
        offer = offer[0]
    else:
        offer = ''

    if contact:
        contact = contact[0]
    else:
        contact = ''

    qs = {
        "intro": intro,
        "offer": offer,
        "pursuits": pursuits,
        "contact": contact,
    }

    return render(request, 'about/index.html', qs)
