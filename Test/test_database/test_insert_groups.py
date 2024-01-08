import unittest
from database.insert_groups import insert_groups, create_session  # Replace 'yourmodule' with the actual module name
from models.groups import Groups


class TestInsertGroups(unittest.TestCase):
    def setUp(self):
        self.filename = "examplefilename"  # replace with the actual filename
        self.grouplist =(
            ("Group1", 30),
            ("Group2", 35),
            ("Group3", 40))

    def testinsertgroups(self):
        insert_groups(self.filename, self.grouplist)
        session = create_session(self.filename)
        result = session.query(Groups).all()
        self.assertEqual(len(result), len(self.grouplist))


if __name__ == '__main__':
    unittest.main()