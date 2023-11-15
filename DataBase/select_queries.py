from DataBase.create_session import create_session
from models.classrooms import Classrooms
from models.groups import Groups
from models.lessons import Lessons
from models.teachers import Teachers
from models.finaldata import FinalData


def getTeacherName(filename, teach_id):
    session = create_session(filename)
    name = session.query(Teachers.fullname).filter(Teachers.teach_id == teach_id).first().fullname
    return name
