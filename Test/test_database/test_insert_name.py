import unittest
from database.insert_name import insert_name, create_session  # replace 'yourmodule' with the actual module name
from models.name import Name

class TestInsertName(unittest.TestCase):
    def setUp(self):
        self.filename = "examplefilename"  # replace with the actual filename
        self.name = "John Doe"

    def testinsertname(self):
        insert_name(self.filename, self.name)
        session = create_session(self.filename)
        result = session.query(Name).filterby(name=self.name).first()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()