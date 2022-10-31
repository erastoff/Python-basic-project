from django.contrib import admin

from .models import Parent, ParentBreed, ParentGender, ParentColor, ParentKennel


@admin.register(ParentBreed, ParentGender, ParentColor)
class UniversalAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description"
    list_display_links = "pk", "name"
    ordering = ("pk",)


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "breed", "gender", "birth"
    list_display_links = "pk", "name"
    ordering = ("pk",)


@admin.register(ParentKennel)
class ParentKennelAdmin(admin.ModelAdmin):
    list_display = "pk", "number", "description"
    list_display_links = (
        "pk",
        "number",
    )
    ordering = ("pk",)
