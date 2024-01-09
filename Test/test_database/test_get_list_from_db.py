import unittest
from database.get_list_from_db import (getTeacherList, getGroupList, getLessonList, getClassroomList,
                                       getLessonsByGroup, getGroupNameList, getCellList)
from models.classrooms import Classrooms
from models.groups import Groups
from models.lessons import Lessons
from models.teachers import Teachers


class TestDBFunctions(unittest.TestCase):
    def setUp(self):
        self.filename = "test.rsp"

    def test_teacher_list(self):
        result = getTeacherList(self.filename)
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, Teachers)

    def test_group_list(self):
        result = getGroupList(self.filename)
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, Groups)

    def test_lesson_list(self):
        result = getLessonList(self.filename)
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, Lessons)

    def test_classroom_list(self):
        result = getClassroomList(self.filename)
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, Classrooms)

    def test_lessons_by_group(self):
        groupname = "somegroupname"
        result = getLessonsByGroup(self.filename, groupname)
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, Lessons)
            self.assertEqual(item.groupname, groupname)

    def test_group_name_list(self):
        result = getGroupNameList(self.filename)
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, str)

    def test_dbname(self):
        result = getCellList(self.filename)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "test.rsp")  # replace with the expected name

if __name__ == '__main__':
    unittest.main()