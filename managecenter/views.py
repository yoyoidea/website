from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.template import loader
from .models import WebSite


def index(request):
    web_site_list = WebSite.objects.all()
    context = {"web_site_list": web_site_list}
    return render(request, 'index.html', context)
