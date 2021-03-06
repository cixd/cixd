from django.shortcuts import render
from apps.projects.models import *
import datetime

def index(request):
    areas = Area.objects.all()

    qs = {
        "areas": areas
    }

    return render(request, 'projects/index.html', qs)

def list(request, _id):
    project = Project.objects.get(id=_id)

    qs = {
        "project": project
    }

    return render(request, 'projects/list.html', qs)

def grants(request):
    today = datetime.date.today()

    grants_gov = Grant.objects.filter(sponsor="GOV", open_date__lte=today).order_by('-start_year')
    grants_cor = Grant.objects.filter(sponsor="COR", open_date__lte=today).order_by('-start_year')

    qs = {
        "grants_gov": grants_gov,
        "grants_cor": grants_cor
    }

    return render(request, 'projects/grants.html', qs)
