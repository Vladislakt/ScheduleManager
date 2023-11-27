from database.create_session import create_session
from models.teachers import Teachers


# Функция для изначального заполнения отношения teachers
def insert_teachers(filename, teacher_list):
    session = create_session(filename)
    for element in teacher_list:
        teacher = Teachers(fullname=element)
        session.add(teacher)
    session.commit()
    session.close()
