from django.contrib import admin

from . import models


# admin.site.register(models.Animal)


@admin.register(models.Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age",
        "kind",
        "is_auto_generated",
        "created_at",
        "modified_at",
    )
    list_filter = (
        "kind",
        "is_auto_generated",
        "created_at",
    )


class AnimalInline(admin.TabularInline):
    model = models.Animal


@admin.register(models.Kind)
class KindAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
        "modified_at",
    )
    inlines = (AnimalInline,)
