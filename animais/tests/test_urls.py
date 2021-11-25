from django.test import TestCase, RequestFactory
from django.urls import resolve
from animais.views import index


class AnimaisURLSTestCase(TestCase):
    def setUp(self) -> None:
        self.request_factory = RequestFactory()

    def test_root_url_use_index_view(self):
        """Testa se a rota raiz da aplicação ('/') utiliza a view index"""

        resolved_path = resolve("/")
        self.assertEqual(resolved_path.func, index)

    def test_index_view_render_index_template(self):
        """Testa se a view index renderiza o template index.html"""

        with self.assertTemplateUsed("index.html"):
            request = self.request_factory.get("/")
            index(request)
