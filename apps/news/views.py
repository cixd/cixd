from django.shortcuts import render
from apps.main.models import CoverImage

def index(request):
    cover_images = CoverImage.objects.exclude(order=0).order_by('date');

    qs = {
        "cover_images": []
    }

    for image in cover_images:
        q = {
            "date": image.date.strftime("%B %d, %Y"),
            "title": image.title,
            "url": image.image.url
        }

        qs["cover_images"].append(q)

    return render(request, 'main/index.html', qs)
