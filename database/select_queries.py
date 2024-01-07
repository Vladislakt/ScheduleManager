from database.create_session import create_session
from models.classrooms import Classrooms
from models.groups import Groups
from models.information import Information
from models.lessons import Lessons
from models.name import Name
from models.teachers import Teachers
from models.cell import Cell


def getTeacherName(filename, teach_id):
    session = create_session(filename)
    name = session.query(Teachers).filter(Teachers.teach_id == teach_id).first().fullname
    return name


def getLesson(filename, lesson_id):
    session = create_session(filename)
    return session.query(Lessons).filter(Lessons.id == lesson_id).first()


def getDBName(filename):
    session = create_session(filename)
    return session.query(Name).first().name


def getIsSaturday(filename):
    session = create_session(filename)
    return session.query(Information).first().isSaturday


def getMaxLesson(filename):
    session = create_session(filename)
    return session.query(Information).first().maxLesson
