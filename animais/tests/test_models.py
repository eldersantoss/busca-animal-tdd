from django.test import TestCase
from model_mommy import mommy


class AnimalModelTests(TestCase):
    def setUp(self) -> None:
        self.animal = mommy.make("Animal")

    def test_animal_str_returns_name(self):
        self.assertEqual(str(self.animal), self.animal.name)

    def test_animal_has_all_characteristics(self):
        """Testa se as instâncias de Animal possuem todas as características
        (atributos) preestabelecidas"""
        self.assertIn("name", dir(self.animal))
        self.assertIn("predator", dir(self.animal))
        self.assertIn("poisonous", dir(self.animal))
        self.assertIn("domestic", dir(self.animal))
