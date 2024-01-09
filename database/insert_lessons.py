from database.create_session import create_session
from models.lessons import Lessons


# Функция для изначального заполнения отношения lessons
def insert_lessons(filename, lesson_list):
    session = create_session(filename)
    for element in lesson_list:
        lesson = Lessons(teach_id=element[0], group_name=element[1], quantity=element[2], lesson_name=element[3],
                         projector=element[4], computers=element[5])
        session.add(lesson)
    session.commit()
    session.close()
