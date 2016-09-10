import unittest

from localizador import LocalizadorService
from datetime import datetime

class LocalizadorTest(unittest.TestCase):

    def setUp(self):
        self.service = LocalizadorService()

    def test_inserirItem(self):
        it = self.service.inserirItem(codigo='lala', nome='lala')
        print(it)

    def test_obterItem(self):
        item = self.service.obterItemPorNome('lala')
        print(item.nome)

    def test_inserirTipoDispositivo(self):
        tipo = self.service.inserirTipoDispositivo('tipoLala', 'nomeLala')
        print(tipo.nome)
        return tipo


    def test_inserirDispositivo(self):
        tipo = self.service.inserirTipoDispositivo('tipoLala', 'nomeLala')
        disp = self.service.inserirDispositivo(tipo, 'dispositivoLala', 'dispositivoLala')
        print(disp.nome)
        return disp

    def test_inserirInstalacao(self):
        tipo = self.service.inserirTipoDispositivo('tipoLala', 'nomeLala')
        disp = self.service.inserirDispositivo(tipo, 'dispositivoLala', 'dispositivoLala')
        it = self.service.inserirItem(codigo='lala', nome='lala')
        inst = self.service.instalarDispositivoNoItem(it, disp)
        print(inst)

    def test_inserirLeitura(self):
        leitura = self.service.inserirLeitura('dispositivoLala', -40.00, -20.00, 0.0, 1)

        print(leitura)

    def test_listarLeiturasDoDispositivo(self):
        #disp = self.service.obterDispositivoPorCodigo('dispositivoLala')
        leituras = self.service.listarLeiturasDeDispositivo('dispositivoLala')
        l = None
        if leituras:
            l = leituras[0]
        print(leituras)
        print(l)


if __name__ == '__main__':
    unittest.main()
