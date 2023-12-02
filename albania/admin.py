from django.contrib import admin

from . import models
from . models import City, Attraction, UserGeneratedContent, Review

# Register your models here.

admin.site.register(Attraction)
admin.site.register(UserGeneratedContent)
admin.site.register(Review)

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'description']
    list_editable = ['description']
