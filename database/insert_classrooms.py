from database.create_session import create_session
from models.classrooms import Classrooms


# Функция для изначального заполнения отношения classrooms
def insert_classrooms(filename, classroom_list):
    session = create_session(filename)
    for element in classroom_list:
        classroom = Classrooms(class_number=element[0], max_size=element[1], projector=element[2], computers=element[3])
        session.add(classroom)
    session.commit()
    session.close()
