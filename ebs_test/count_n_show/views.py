import random
from urllib.parse import urljoin

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    cdn_url = settings.CDN_URL
    chosen_one = f"{random.choice(range(1, 6))}.jpg"
    url = urljoin(cdn_url, chosen_one)
    return render(request, "show/template.html", context={"url": url})
