from django.contrib import admin
from .models import Experience, Perk

# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "price",
        "start",
        "end",
        "host",
        "created_at",
    )

    list_filter = (
        "category",
        "city",
        "perks",
        "created_at",
        "updated_at",
    )


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "details",
        "explanation",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
