from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Animal, Observ

class ObservTest(TestCase):
    def setUp(self):
        self.animal = Animal.objects.create(
            nom_commun="Renard",
            description="Un renard roux",
        )
        self.observ = Observ.objects.create(
            date_heure=timezone.now(),
            latitude=47.9,
            longitude=1.9,
            animal=self.animal,
            description="Observation test",
        )

    def test_animal_str(self):
        self.assertEqual(str(self.animal), "Renard")

    def test_observ_str(self):
        self.assertIn("Renard", str(self.observ))

    def test_animal_list_view(self):
        response = self.client.get(reverse("animal_list"))
        self.assertEqual(response.status_code, 200)

    def test_observ_detail_view(self):
        response = self.client.get(reverse("observ_list"))
        self.assertIn(response.status_code, [200,302])

