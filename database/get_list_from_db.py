from database.create_session import create_session
from models.classrooms import Classrooms
from models.groups import Groups
from models.information import Information
from models.lessons import Lessons
from models.name import Name
from models.teachers import Teachers
from models.finaldata import FinalData


def getTeacherList(filename):
    session = create_session(filename)
    list = session.query(Teachers).all()
    return list


def getGroupList(filename):
    session = create_session(filename)
    list = session.query(Groups).all()
    return list


def getLessonList(filename):
    session = create_session(filename)
    list = session.query(Lessons).all()
    return list


def getClassroomList(filename):
    session = create_session(filename)
    list = session.query(Classrooms).all()
    return list


def getLessonsByGroup(filename, group_name):
    session = create_session(filename)
    list = session.query(Lessons).filter(Lessons.group_name == group_name).all()
    return list


def getGroupNameList(filename):
    session = create_session(filename)
    list = []
    for group in session.query(Groups).all():
        list.append(group.group_name)
    return list


def getDBName(filename):
    session = create_session(filename)
    return session.query(Name).first().name


def getIsSaturday(filename):
    session = create_session(filename)
    return session.query(Information).first().isSaturday


def getMaxLesson(filename):
    session = create_session(filename)
    return session.query(Information).first().maxLesson
