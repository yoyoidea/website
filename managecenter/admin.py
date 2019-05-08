from django.contrib import admin

# Register your models here.
from .models import WebSite, WebSiteType


# Register your models here.
@admin.register(WebSiteType)
class MangeWebSite(admin.ModelAdmin):
    list_display = ('name', 'icon', 'rank')


@admin.register(WebSite)
class MangeWebSite(admin.ModelAdmin):
    list_display = ('title', 'type', 'logo_url', )

