from database.create_session import create_session
from models.information import Information


# Функция для изначального заполнения отношения information
def insert_information(filename, isSaturday, maxLesson):
    session = create_session(filename)
    new_information = Information(isSaturday=isSaturday, maxLesson=maxLesson)
    session.add(new_information)
    session.commit()
    session.close()
