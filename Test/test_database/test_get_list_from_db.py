import unittest
from database.get_list_from_db import (
    getTeacherList, getGroupList, getLessonList, getClassroomList,
    getLessonsByGroup, getGroupNameList, getDBName
)  # replace 'yourmodule' with the actual module name
from database.create_session import create_session
from models.classrooms import Classrooms
from models.groups import Groups
from models.lessons import Lessons
from models.name import Name
from models.teachers import Teachers
from models.finaldata import FinalData

class TestDBFunctions(unittest.TestCase):
    def setUp(self):
        self.filename = "examplefilename"  # replace with the actual filename

    def testteacherlist(self):
        result = getTeacherList(self.filename)
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, Teachers)

    def testgrouplist(self):
        result = getGroupList(self.filename)
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, Groups)

    def testlessonlist(self):
        result = getLessonList(self.filename)
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, Lessons)

    def testclassroomlist(self):
        result = getClassroomList(self.filename)
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, Classrooms)

    def testlessonsbygroup(self):
        groupname = "somegroupname"
        result = getLessonsByGroup(self.filename, groupname)
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, Lessons)
            self.assertEqual(item.groupname, groupname)

    def testgroupnamelist(self):
        result = getGroupNameList(self.filename)
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, str)

    def testdbname(self):
        result = getDBName(self.filename)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "somedbname")  # replace with the expected name

if __name__ == '__main__':
    unittest.main()