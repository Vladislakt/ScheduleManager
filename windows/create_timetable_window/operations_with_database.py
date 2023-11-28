from database.get_list_from_db import getLessonsByGroup, getClassroomList, getGroupList
from database.select_queries import getTeacherName


def get_groups(db):
    return getGroupList(db)


def get_classrooms(db):
    return getClassroomList(db)


def get_group_names(db):
    names = []
    groups = get_groups(db)
    for group in groups:
        names.append(group.group_name)
    return names


def get_courses(db):
    courses_for_all_groups = []
    group_names = get_group_names(db)
    for group in group_names:
        courses_for_all_groups.append(getLessonsByGroup(db, group))
    return courses_for_all_groups


def get_courses_with_teachers(db):
    courses_teachers = []
    courses = get_courses(db)
    for i in range(len(courses)):
        one_group = []
        for j in range(len(courses[i])):
            one_group.append(f"{courses[i][j].lesson_name} ({getTeacherName(db, courses[i][j].teach_id)})")
        courses_teachers.append(one_group)
    return courses_teachers
