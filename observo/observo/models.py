from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Animal(models.Model):

    IUCN_CHOICES = [
        ("LC", "Préoccupation mineure"),
        ("NT", "Quasi menacé"),
        ("VU", "Vulnérable"),
        ("EN", "En danger"),
        ("CR", "En danger critique"),
        ("DD", "Données insuffisantes"),
    ]

    nom_commun = models.CharField(max_length=100)
    nom_savant = models.CharField(max_length=150)

    embranchement = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)
    ordre = models.CharField(max_length=100)
    sous_ordre = models.CharField(max_length=100, blank=True)
    famille = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    statut_iucn = models.CharField(max_length=5, choices=IUCN_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.nom_commun


class Observ(models.Model):
    date_heure = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="observations",
    )

    def __str__(self):
        return f"Observation de {self.animal} le {self.date_heure}"
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey("Animal", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "animal")

    def __str__(self):
        return f"{self.user.username} ♥ {self.animal.nom_commun}"