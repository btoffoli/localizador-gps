from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, func, funcfilter, Table
from sqlalchemy.orm import sessionmaker
from geoAlchemy2ExtensaoPostgis import Geometry, WKTElement


m = MetaData(schema="azimute")
engine = create_engine('postgresql://geocontrol:geo007@localhost:5432/azimute')
Base = automap_base(bind=engine, metadata=m)
Base.prepare(engine, reflect=True)
print(Base.classes.keys())

Leitura = Base.classes.leitura

print(dir(Leitura))


leitura_reflected = Table('leitura', m, autoload=True, autoload_with=engine)

print("leitura_reflected=%s" % leitura_reflected.c)

resp = leitura_reflected.c.status_gps == '2'

print("resp = %s" % resp)


print(Leitura)

Session = sessionmaker(bind=engine)

#Session.configure()

sessao = Session()

# l = sessao.query(Leitura, func.ST_X(Leitura.localizacao).label('longitude')).first()
l = sessao.query(Leitura).first()

print('%s' % l.localizacao.lon)





