import unittest
from database.insert_teachers import insert_teachers, create_session
from models.teachers import Teachers

class TestInsertTeachers(unittest.TestCase):
    def setUp(self):
        self.filename = "test.rsp"
        self.teacher_list = ["Teacher1", "Teacher2", "Teacher3"]

    def test_insert_teachers(self):
        insert_teachers(self.filename, self.teacher_list)
        session = create_session(self.filename)
        result = session.query(Teachers).all()
        self.assertEqual(len(result), len(self.teacher_list))
        for teacher in result:
            self.assertIn(teacher.fullname, self.teacher_list)

if __name__ == '__main__':
    unittest.main()