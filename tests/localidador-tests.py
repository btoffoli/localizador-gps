import unittest
from localizador import LocalizadorService

class LocalizadorTest(unittest.TestCase):

    def setUp(self):
        self.service = LocalizadorService()

    def test_inserirItem(self):
        self.service.inserirItem(codigo='lala', nome='lala')



if __name__ == '__main__':
    unittest.main()
