from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class __DBConfig:

    def __init__(self):
        self.__sessionFactory = sessionmaker(bind=self.poolEngine)

    @property
    def url(self):
        return 'postgresql://geocontrol:geo007@localhost:5432/azimute'

    @property
    def schema(self):
        return 'azimute'

    @property
    def poolEngine(self):
        return create_engine(self.url, pool_size=20, max_overflow=0)

    @property
    def sessionFactory(self):
        if not self.__sessionFactory:
            self.__sessionFactory = sessionmaker(bind=self.poolEngine)
        return self.__sessionFactory

    @property
    def session(self):
        #TODO verificar app qnd for thread de verdade
        return self.sessionFactory()




dbConfig = __DBConfig()