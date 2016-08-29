import datetime

from config import dbConfig
from db.localizador_db import Dispositivo
from models import Item, Leitura, Instalacao, TipoDispositivo
from datetime import datetime


class LocalizadorService:

    # TODO metodo inserirDispositivo, mapear tipo_dispositivo
    # TODO mapear dispositvo e item em instalacao implementar teste p/ verificar
    #

    @property
    def __sessao(self):
        dbConfig.session()

    def inserirDispositivo(self, tipo, codigo, nome, commit=True):
        disp = self.obterDispositivoPorCodigo()
        if not disp:
            disp = Dispositivo(tipo=tipo, nome=nome, codigo=codigo)
            self.__sessao.add(disp)
            if commit:
                self.__sessao.commit()
        return disp

    def inserirTipoDispositivo(self, codigo, nome, commit=True):
        tpDisp = self.obterTipoDispositivoPorCodigo()
        if not tpDisp:
            tpDisp = TipoDispositivo(nome=nome, codigo=codigo)
            self.__sessao.add(tpDisp)
            if commit:
                self.__sessao.commit()
        return tpDisp

    def instalarDispositivoNoItem(self, item, dispositivo, data_instalacao=datetime.now(), commit=True):
        inst = Instalacao(item=item, dispositivo=dispositivo, data_instalacao=data_instalacao)
        sessao = self.__sessao
        sessao.add(inst)
        if commit:
            sessao.commit()

        return inst



    def inserirItem(self, nome, codigo, commit=True):
        sessao = dbConfig.session()

        it = self.obterItemPorCodigo(codigo)
        if not it:
            it = Item(nome=nome, codigo=codigo)
            sessao.add(it)
        #Verificar existencia do item, codigo e instalacao
        if commit:
            sessao.commit()
        return it

    def obterInstalacaoEmAbertoPorItemEDispositivo(self, item, dispositivo):
        instalacao = None
        q = dbConfig.session().query(Instalacao).filter(Item == item, )
        itens = q.all()
        if itens:
            item = itens[0]
        return item

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

    def obterDispositivoPorCodigo(self, codigo):
        dispositivo = None
        q = dbConfig.session().query(Dispositivo).filter(Dispositivo.codigo == codigo)
        dispositivos = q.all()
        if dispositivos:
            dispositivo = dispositivos[0]
        return dispositivo

    def inserirLeitura(self, identificacao, dataHora, longitude, latitude, commit=True):
        item = self.obterItemPorCodigo(identificacao)
        if item:
            leitura = Leitura(horario_leitura=dataHora, localizacao="POINT(%f %f)" %(longitude, latitude))
            sessao = dbConfig.session()
            sessao.add(leitura)
            if commit:
                sessao.commit()
            return leitura
        return

    def obterTipoDispositivoPorCodigo(self, codigo):
        tpDisp = None
        q = dbConfig.session().query(Dispositivo).filter(Dispositivo.codigo == codigo)
        tipos = q.all()
        if tipos:
            tpDisp = tipos[0]
        return tpDisp

    def inserirItemCompleto(self, nomeItem, codigoItem, nome):
        pass






