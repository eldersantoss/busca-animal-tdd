from django.test import TestCase
from model_mommy import mommy


class IndexViewTests(TestCase):
    def setUp(self) -> None:
        self.animal = mommy.make("Animal")

    def test_index_view_render_index_template(self):
        """Testa se a view index renderiza corretamente o template no primeiro
        acesso (sem inputs)"""

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_index_view_returns_animal_characteristics_when_input_was_filled(self):
        """Testa se a view index retorna os dados das características do animal
        cujo nome foi passado como entrdada"""

        response = self.client.get("/", {"animal": str(self.animal)})
        animal_data = response.context["animals"][0]
        self.assertIn("name", dir(animal_data))
        self.assertIn("predator", dir(animal_data))
        self.assertIn("poisonous", dir(animal_data))
        self.assertIn("domestic", dir(animal_data))
