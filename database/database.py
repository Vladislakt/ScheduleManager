from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Базовый класс для создания бд
Base = declarative_base()


# Фунция создания бд по соединению
def create_db(filename):
    database_name = f'finaldata/{filename}.sqlite'
    engine = create_engine(f'sqlite:///{database_name}')
    Base.metadata.create_all(engine)
