from django.test import TestCase

from animais.models import Animal


class AnimalModelTests(TestCase):
    def setUp(self) -> None:
        self.animal = Animal.objects.create(
            name="gato",
            predator=False,
            poisonous=False,
            domestic=True,
        )

    def test_animal_has_all_characteristics(self):
        """Testa se as instâncias de Animal possuem todas as características
        (atributos) preestabelecidas"""
        self.assertIn("name", dir(self.animal))
        self.assertIn("predator", dir(self.animal))
        self.assertIn("poisonous", dir(self.animal))
        self.assertIn("domestic", dir(self.animal))
