from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, func, funcfilter
from sqlalchemy.orm import sessionmaker
from geoAlchemy2ExtensaoPostgis import Geometry, WKTElement



m = MetaData(schema="azimute")
engine = create_engine('postgresql://geocontrol:geo007@localhost:25432/azimute')
Base = automap_base(bind=engine, metadata=m)
Base.prepare(engine, reflect=True)
print(Base.classes.keys())

Leitura = Base.classes.leitura

print(dir(Leitura))


print(Leitura)

Session = sessionmaker(bind=engine)

#Session.configure()

sessao = Session()

l = sessao.query(Leitura, func.ST_X(Leitura.localizacao).label('longitude')).first()

print('%f' % l.longitude)





