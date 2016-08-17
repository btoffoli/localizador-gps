import sqlalchemy
from geoalchemy2.types import Geography
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, func, funcfilter
from sqlalchemy.orm import sessionmaker
from geoAlchemy2ExtensaoPostgis import Geometry, WKTElement
from config import dbConfig
from sqlalchemy.sql.schema import Column

__m = MetaData(schema=dbConfig.schema)
__engine = create_engine(dbConfig.url)
__m.reflect(__engine, only=['tipo_dispositivo', 'dispositivo', 'item', 'instalacao'])
__Base = automap_base(bind=__engine, metadata=__m)
__Base.prepare(__engine, reflect=True)
# print(Base.classes.keys())
#tipo_dispositivo', 'leitura', 'dispositivo', 'item', 'instalacao
#LeituraAutomap = __Base.classes.leitura
TipoDispositivo = __Base.classes.tipo_dispositivo
Dispositivo = __Base.classes.dispositivo

"""
    Fields:
    codigo       | character varying(255)   | not null
    nome         | character varying(255)   | not null
    atributos    | public.hstore            | not null default ''::public.hstore
"""
Item = __Base.classes.item
Instalacao = __Base.classes.instalacao
Leitura = __Base.classes.leitura


#class Leitura(__Base, __Base.classes.leitura):
#    __tablename__ = 'leitura'
#    __table_args__ = {'extend_existing': True}
#    horario_leitura = Column('horario_leitura', sqlalchemy.types.DateTime)
#    localizacao = Column('localizacao', Geography(geometry_type='POINT', srid=4326))


