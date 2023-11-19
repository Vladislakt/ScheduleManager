from DataBase.get_list_from_db import getGroupNameList, getLessonsByGroup, getClassroomList, getGroupList
from DataBase.select_queries import getTeacherName

db = "test"

group_names = getGroupNameList(db)
len_group_names = len(group_names)
groups = getGroupList(db)
classrooms = getClassroomList(db)


def get_courses_with_teachers():
    courses = []
    for group in group_names:
        lessons = getLessonsByGroup(db, group)
        courses_for_one_group = []
        for i in range(len(lessons)):
            courses_for_one_group.append(f"{lessons[i].lesson_name} ({getTeacherName(db, lessons[i].teach_id)})")
        courses.append(courses_for_one_group)
    return courses


courses_with_teachers = get_courses_with_teachers()


def get_courses():
    courses_for_all_groups = []
    for i in range(len(group_names)):
        courses_for_all_groups.append(getLessonsByGroup(db, group_names[i]))
    return courses_for_all_groups


courses = get_courses()
