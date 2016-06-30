from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, func, funcfilter
from sqlalchemy.orm import sessionmaker
from geoAlchemy2ExtensaoPostgis import Geometry, WKTElement
from config import dbConfig


__m = MetaData(schema=dbConfig.schema)
__engine = create_engine(dbConfig.url)
__Base = automap_base(bind=__engine, metadata=__m)
__Base.prepare(__engine, reflect=True)
# print(Base.classes.keys())
#tipo_dispositivo', 'leitura', 'dispositivo', 'item', 'instalacao
Leitura = __Base.classes.leitura
TipoDispositivo = __Base.classes.tipo_dispositivo
Dispositivo = __Base.classes.dispositivo
Item = __Base.classes.item
Instalacao = __Base.classes.instalacao

