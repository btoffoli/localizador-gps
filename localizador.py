from config import dbConfig
from db.localizador_db import Dispositivo
from models import Item, Leitura, Instalacao

class LocalizadorService:

    def inserirItem(self, **kwargs):
        nome = kwargs.get('nome')
        codigo = kwargs.get('codigo')
        nomeDispositivo = kwargs.get('nomeDispositivo')
        self
        sessao = dbConfig.session()

        it = self.obterItemPorCodigo(codigo)
        if not it:
            it = Item(nome=nome, codigo=codigo)
            sessao.add(it)



        sessao.commit()
        return it


    def obterItemPorNome(self, nome):
        item = None
        q = dbConfig.session().query(Item).filter(Item.nome==nome)
        itens = q.all()
        if itens:
            item = itens[0]
        return item

    def obterItemPorCodigo(self, codigo):
        item = None
        q = dbConfig.session().query(Item).filter(Item.codigo == codigo)
        itens = q.all()
        if itens:
            item = itens[0]
        return item

    def obterDispositivoPorNome(self, nome):
        dispositivo = None
        q = dbConfig.session().query(Dispositivo).filter(Dispositivo.nome == nome)
        dispositivos = q.all()
        if dispositivos:
            dispositivo = dispositivos[0]
        return dispositivo

    def inserirLeitura(self, identificacao, dataHora, longitude, latitude):
        item = self.obterItemPorCodigo(identificacao)
        if item:
            leitura = Leitura(horario_leitura=dataHora, localizacao="POINT(%f %f)" %(longitude, latitude))
            sessao = dbConfig.session()
            sessao.add(leitura)
            sessao.commit()
            return leitura
        return







