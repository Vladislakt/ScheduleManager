from DataBase.create_session import create_session

from models.teachers import Teachers
from models.lessons import Lessons
from models.finaldata import FinalData


def SELECTING(filename):
    session = create_session(filename)
    t = session.query(Teachers).first()
    print(t)

SELECTING("test")