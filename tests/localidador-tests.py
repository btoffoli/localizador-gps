import unittest
from localizador import LocalizadorService
from datetime import datetime

class LocalizadorTest(unittest.TestCase):

    def setUp(self):
        self.service = LocalizadorService()

    def test_inserirItem(self):
        self.service.inserirItem(codigo='lala', nome='lala')

    def test_obterItem(self):
        item = self.service.obterItemPorNome('lala')
        print(item.nome)

    def test_inserirTipoDispositivo(self):
        tipo = self.service.inserirTipoDispositivo('tipoLala', 'nomeLala')
        print(tipo.nome)


    # def test_inserirDispositivo(self):
    #     self.service.inserirDispositivo()

    # def test_inserirLeitura(self):
    #     leitura = self.service.inserirLeitura('lala', datetime.now(), -40.00, -20.00)




if __name__ == '__main__':
    unittest.main()
