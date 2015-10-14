from django.shortcuts import render
from apps.main.models import CoverImage
from apps.news.models import Article
from apps.projects.models import Area

def index(request):
    cover_images = CoverImage.objects.exclude(order=0).order_by('order', 'date')
    news_articles = Article.objects.order_by('-date')[:6]
    areas = Area.objects.all()

    qs = {
        "cover_images": cover_images,
        "news_articles": news_articles,
        "areas": areas
    }

    return render(request, 'main/index.html', qs)
