from django.shortcuts import render
from apps.people.models import Member

def members(request):
    professors = Member.objects.filter(phase="PROF").order_by('year')
    phd_students = Member.objects.filter(phase="PHD").order_by('year')
    m_students = Member.objects.filter(phase="M").order_by('year')

    qs = {
        "professors": professors,
        "phd_students": phd_students,
        "m_students": m_students
    }

    return render(request, 'people/members.html', qs)

def alumni(request):
    phds = Member.objects.filter(phase="PHDG")
    masters = Member.objects.filter(phase="MG")

    qs = {
        "phds": phds,
        "masters": masters
    }

    return render(request, 'people/alumni.html', qs)
