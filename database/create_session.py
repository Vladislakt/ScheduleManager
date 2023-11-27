import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Функция для открытия сессии для работы с бд
def create_session(filename):
    database_name = f"finaldata/{filename}.rsp"
    while True:
        if os.path.isfile(database_name):
            break
        else:
            database_name = "../" + database_name
    engine = create_engine(f'sqlite:///{database_name}')
    Session = sessionmaker(bind=engine)
    return Session()
