from database.get_list_from_db import getLessonsByGroup, getClassroomList, getGroupList, getCellList
from database.save_functions import save_finaldata
from database.select_queries import getTeacherName
from models.cell import Cell


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


def get_cells(db):
    return getCellList(db)


def write_table_data_to_db(db, table, days, number_of_classes_per_day):
    data_array = []
    for i in range(len(table.group_names)):
        for j in range(len(days)):
            for k in range(number_of_classes_per_day):
                selected_course_index = table.scroll_area_layout.itemAtPosition(
                    j * (number_of_classes_per_day + 1) + k + 2,
                    3 + i * 3).widget().currentIndex()
                classroom_value = table.scroll_area_layout.itemAtPosition(
                    j * (number_of_classes_per_day + 1) + k + 2,
                    4 + i * 3).widget().currentText()
                if selected_course_index == -1:
                    if classroom_value == "":
                        continue
                    else:
                        course_id = None
                else:
                    if classroom_value == "":
                        classroom_value = None
                    course_id = table.courses[i][selected_course_index - 1].id
                cell = Cell(table.group_names[i], days[j], k + 1, course_id, classroom_value)
                data_array.append(cell)
                print(table.courses[i][selected_course_index - 1])
                print(cell.group, cell.day, cell.number_of_class, cell.lesson_id, cell.classroom, "\n")
    save_finaldata(db, data_array)
