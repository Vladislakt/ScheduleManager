from database.create_session import create_session
from models.name import Name


# Функция для изначального заполнения отношения name
def insert_name(filename, name):
    session = create_session(filename)
    new_name = Name(name=name)
    session.add(new_name)
    session.commit()
    session.close()
