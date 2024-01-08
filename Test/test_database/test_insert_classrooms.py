import unittest
from database.insert_classrooms import insert_classrooms  # Replace 'yourmodule' with the actual module name
from database.create_session import create_session
from models.finaldata import FinalData
from models.classrooms import Classrooms


class TestInsertClassrooms(unittest.TestCase):
    def setUp(self):
        self.filename = "examplefilename"  # replace with the actual filename
        self.classroomlist =(
            (1, 30, True, 20),
            (2, 35, True, 25),
            (3, 40, False, 30))


    def testinsertclassrooms(self):
        insert_classrooms(self.filename, self.classroomlist)
        session = create_session(self.filename)
        result = session.query(Classrooms).all()
        self.assertEqual(len(result), len(self.classroomlist))


if __name__ == '__main__':
    unittest.main()