from django.shortcuts import render
from apps.news.models import Article
from datetime import date

def list(request):
    s_year = 2008
    e_year = date.today().year

    years = []

    for y in reversed(range(s_year, e_year + 1)):
        years.append({
            "year": y,
            "list": Article.objects.filter(date__year=y)
        })

    qs = {
        "years": years
    }

    return render(request, 'news/index.html', qs)

def detail(request, _id):
    article = Article.objects.get(id=_id)

    qs = {
        "article": article
    }

    return render(request, 'news/detail.html', qs)
