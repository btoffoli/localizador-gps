from models import Leitura
from config import dbConfig

sessao = dbConfig.session
l = sessao.query(Leitura).first()

print(l.localizacao)