from django.contrib import admin

from .models import Puppy, PuppyStatus#, PuppyBreed


@admin.register(PuppyStatus)#, PuppyBreed)
class UniversalPuppyAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description"
    list_display_links = "pk", "name"


@admin.register(Puppy)
class PuppyAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "birth", "description"
    list_display_links = "pk", "name"
    ordering = "pk",
