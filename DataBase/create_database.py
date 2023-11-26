from DataBase.database import create_db
from models.teachers import Teachers
from models.groups import Groups
from models.lessons import Lessons
from models.classrooms import Classrooms
from models.finaldata import FinalData
from models.name import Name


# Функция для создания бд из окружения
def create_database(filename):
    create_db(filename)
