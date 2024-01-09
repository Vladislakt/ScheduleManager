import unittest
from database.insert_lessons import insert_lessons, create_session
from models.lessons import Lessons


class TestInsertLessons(unittest.TestCase):
    def setUp(self):
        self.filename = "test.rsp"
        self.lessonlist =(
            (1, "Group1", 20, "Math", True, 10),
            (2, "Group2", 25, "Science", False, 15),
            (3, "Group3", 30, "English", True, 20))


    def test_insert_lessons(self):
        insert_lessons(self.filename, self.lessonlist)
        session = create_session(self.filename)
        result = session.query(Lessons).all()
        self.assertEqual(len(result), len(self.lessonlist))


if __name__ == '__main__':
    unittest.main()