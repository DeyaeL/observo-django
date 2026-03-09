from django.contrib import admin
from .models import Animal, Observ


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ("nom_commun", "nom_savant", "statut_iucn", "famille", "genre")
    search_fields = ("nom_commun", "nom_savant", "famille", "genre")
    list_filter = ("statut_iucn", "classe", "ordre")


@admin.register(Observ)
class ObservAdmin(admin.ModelAdmin):
    list_display = ("id", "animal", "date_heure", "user")
    list_filter = ("date_heure", "animal")
