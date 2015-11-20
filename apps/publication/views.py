from django.shortcuts import render
from apps.publication.models import Category, Publication

def index(request):
    ctgs = Category.objects.all()

    qs = {
        "ctgs": ctgs
    }

    return render(request, 'publication/index.html', qs)
