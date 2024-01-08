import unittest
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

class TestCreateDatabase(unittest.TestCase):

    def test_create_database_path_exists(self):
        path = "finaldata"
        self.assertTrue(os.path.isdir(path))

    def test_create_database_filename_exists(self):
        filename = ""
        for i in range(8):
            filename += random.choice(string.ascii_letters)
        path = "finaldata"
        while True:
            if not os.path.isfile(path + "/" + filename + ".rsp"):
                create_db(filename)
                self.assertTrue(os.path.isfile(path + "/" + filename + ".rsp"))
                break

if __name__ == '__main__':
    unittest.main()