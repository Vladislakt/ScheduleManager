import os
import string
import random

from database.database import create_db
from models.teachers import Teachers
from models.groups import Groups
from models.lessons import Lessons
from models.classrooms import Classrooms
from models.finaldata import FinalData
from models.name import Name


# Функция для создания бд из окружения
def create_database():
    path = "finaldata"
    while True:
        if os.path.isdir(path):
            break
        else:
            path = "../" + path
    while True:
        filename = ""
        for i in range(8):
            filename += random.choice(string.ascii_letters)
        if not os.path.isfile(path + "/" + filename + ".rsp"):
            create_db(filename)
            break
    return filename
