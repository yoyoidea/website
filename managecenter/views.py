# Create your views here.
from django.shortcuts import render
from .models import WebSite, WebSiteType


def index(request):

    web_type_list = WebSiteType.objects.all()
    new_web_site_list = []
    for web_type in web_type_list:
        web_site_list = WebSite.objects.filter(type=web_type)
        if web_site_list:
            new_web_site_list.append({'web_site_type': web_type, 'web_site_list': web_site_list})
    context = {"web_sites": new_web_site_list}
    return render(request, 'index.html', context)
