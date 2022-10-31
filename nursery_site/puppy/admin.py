from django.contrib import admin

from .models import Puppy, PuppyStatus, PuppyBreed, PuppyColor, PuppyGender, PuppyBrood


@admin.register(PuppyStatus, PuppyBreed, PuppyColor, PuppyGender)
class UniversalPuppyAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description"
    list_display_links = "pk", "name"


@admin.register(PuppyBrood)
class PuppyBroodAdmin(admin.ModelAdmin):
    list_display = "pk", "date", "sire", "bitch"
    list_display_links = "pk", "date"


@admin.register(Puppy)
class PuppyAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description"
    list_display_links = "pk", "name"
    ordering = ("pk",)
