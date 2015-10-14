from django.shortcuts import render
from apps.publication.models import Publication

def index(request):
    pubs_jour = Publication.objects.filter(publish_to="JOUR").order_by('date')
    pubs_conf = Publication.objects.filter(publish_to="CONF").order_by('date')

    qs = {
        "pubs_jour": pubs_jour,
        "pubs_conf": pubs_conf
    }

    return render(request, 'publication/journal.html', qs)
