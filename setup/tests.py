from django.test import LiveServerTestCase
from selenium import webdriver


class AnimaisTestCase(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_looking_for_animal(self):
        """Testa se usuário consegue encontrar um animal pesquisando no app"""

        # Usuário acessa sistema
        self.browser.get(self.live_server_url)
        self.assertEqual(self.browser.title, "Busca Animais")

        # Usuário encontra input com placeholder para pesquisar por animal
        input_animal = self.browser.find_element_by_id("animal")
        self.assertEqual(
            input_animal.get_attribute("placeholder"),
            "Exemplo: gato, cachorro, leão...",
        )

        # Usuário digita "leão" e clica no botão pesquisar
        input_animal.send_keys("leão")
        self.browser.find_element_by_id("pesquisar").click()

        # Usuário recebe como resposta 4 características do animal pesquisado
        animals_characteristics = self.browser.find_elements_by_class_name(
            "result-description"
        )
        self.assertAlmostEquals(len(animals_characteristics), 4)
