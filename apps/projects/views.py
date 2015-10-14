from django.shortcuts import render
from apps.projects.models import *
import datetime

def index(request):
    areas = Area.objects.all()

    qs = {
        "areas": areas
    }

    return render(request, 'projects/index.html', qs)

def project(request, name):
    title = name.lower()
    project = Project.objects.get(title__icontains=title)

    qs = {
        "project": project
    }

    return render(request, 'projects/project.html', qs)

def grants(request):
    today = datetime.date.today()

    grants_gov = Grant.objects.filter(sponsor="GOV", open_date__lte=today).order_by('start_year')
    grants_cor = Grant.objects.filter(sponsor="COR", open_date__lte=today).order_by('start_year')

    qs = {
        "grants_gov": grants_gov,
        "grants_cor": grants_cor
    }

    return render(request, 'projects/grants.html', qs)
