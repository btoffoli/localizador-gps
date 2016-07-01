from config import dbConfig
from models import Item

class LocalizadorService:

    def inserirItem(self, **kwargs):
        it = Item(kwargs)
        dbConfig.session.add(it)



