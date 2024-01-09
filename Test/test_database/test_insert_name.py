import unittest
from database.insert_name import insert_name, create_session
from models.name import Name

class TestInsertName(unittest.TestCase):
    def setUp(self):
        self.filename = "test.rsp"
        self.name = "John Doe"

    def test_insert_name(self):
        insert_name(self.filename, self.name)
        session = create_session(self.filename)
        result = session.query(Name).filterby(name=self.name).first()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()