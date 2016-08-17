# localizador_db.py
# -*- coding: utf-8 -*-
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, func, funcfilter
from sqlalchemy.orm import sessionmaker


m = MetaData(schema="azimute")
engine = create_engine('postgresql://geocontrol:geo007@localhost:25432/azimute')
Base = automap_base(bind=engine, metadata=m)
Base.prepare(engine, reflect=True)
#Base.classes.keys()

Leitura1 = Base.classes.leitura
class Leitura(Base):
    __tablename__ = 'leitura'


Item = Base.classes.item
Dispositivo = Base.classes.leitura

