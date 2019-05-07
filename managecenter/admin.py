from django.contrib import admin

# Register your models here.
from .models import WebSite, WebSiteType


# Register your models here.
@admin.register(WebSiteType)
class MangeWebSite(admin.ModelAdmin):
    fields = ('name',)


@admin.register(WebSite)
class MangeWebSite(admin.ModelAdmin):
    fields = ('title', 'type', 'picture_url', )

