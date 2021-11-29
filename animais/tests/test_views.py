from django.test import TestCase


class IndexViewTestCase(TestCase):
    def test_index_view_returns_animal_characteristics(self):
        """Testa se a view index retorna os dados das características dos animais

        1. A view index deve receber a requisição do tipo GET e extrair o query
        param de chave 'animal' referente ao nome do animal.

        2. Após extrair o nome do animal dos query params da requisição, deve ser
        realizada uma busca na base de dados por uma instância de animal cujo nome
        seja compatível ao que foi fornecido.

            2.1. Caso o animal seja encontrado: deve ser retornada a renderização do
            template index junto com um objeto de contexto contendo as informações
            extraídas dos atributos da instância na chave 'animal_characteristics'.

            2.2. Caso o animal não seja encontrado: deve ser retornada a renderização
            do template index junto com um objeto de contexto contendo um dicionário
            vazio na chave 'animal_characteristics'.

        """
