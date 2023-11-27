from DataBase.get_list_from_db import getLessonsByGroup, getClassroomList, getGroupList
from DataBase.select_queries import getTeacherName

db = "test"

groups = getGroupList(db)
classrooms = getClassroomList(db)


def get_group_names():
    names = []
    for group in groups:
        names.append(group.group_name)
    return names


group_names = get_group_names()


def get_courses():
    courses_for_all_groups = []
    for group in group_names:
        courses_for_all_groups.append(getLessonsByGroup(db, group))
    return courses_for_all_groups


courses = get_courses()


def get_courses_with_teachers():
    courses_teachers = []
    for i in range(len(courses)):
        one_group = []
        for j in range(len(courses[i])):
            one_group.append(f"{courses[i][j].lesson_name} ({getTeacherName(db, courses[i][j].teach_id)})")
        courses_teachers.append(one_group)
    return courses_teachers


courses_with_teachers = get_courses_with_teachers()
