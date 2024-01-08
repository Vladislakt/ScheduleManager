import unittest
from database.select_queries import getTeacherName, create_session  # Replace 'your_module' with the actual module name
from models.teachers import Teachers

class TestGetTeacherName(unittest.TestCase):
    def setUp(self):
        self.filename = "example_filename"  # replace with the actual filename
        self.teach_id = 1
        self.fullname = "John Doe"
        with create_session(self.filename) as session:
            teacher = Teachers(teach_id=self.teach_id, fullname=self.fullname)
            session.add(teacher)
            session.commit()

    def test_get_teacher_name(self):
        result = getTeacherName(self.filename, self.teach_id)
        self.assertEqual(result, self.fullname)

if __name__ == '__main__':
    unittest.main()
