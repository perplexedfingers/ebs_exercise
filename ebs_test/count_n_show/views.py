import random
from urllib.parse import urljoin

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import Count

picture_count = 5


@csrf_exempt
def index(request):
    if request.method == "POST":
        Count.objects.create()
        return HttpResponse("OK")
    elif request.method == "GET":
        cdn_url = settings.CDN_URL
        count = Count.objects.count()
        chosen_one = f"{(count % picture_count) + 1}.jpg"
        url = urljoin(cdn_url, chosen_one)
        return render(request, "show/template.html", context={"url": url})
