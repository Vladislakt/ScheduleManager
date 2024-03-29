from database.create_session import create_session
from models.classrooms import Classrooms
from models.groups import Groups
from models.lessons import Lessons
from models.teachers import Teachers
from models.cell import Cell


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


def getCellList(filename):
    session = create_session(filename)
    list = session.query(Cell).all()
    return list
