def check_new_bd_name(new_name):
    return new_name != ""


def check_teachers_data(teacher_list):
    if len(teacher_list) == 1:
        return False
    for index in range(1, len(teacher_list)):
        if teacher_list[index].teacher.text() == "":
            return False
    return True


def check_groups_data(group_list):
    if len(group_list) == 1:
        return False
    for index in range(1, len(group_list)):
        if group_list[index].group.text() == "" or group_list[index].size.text() == "":
            return False
    return True


def check_classrooms_data(classroom_list):
    if len(classroom_list) == 1:
        return False
    for index in range(1, len(classroom_list)):
        if classroom_list[index].classroom.text() == "" or classroom_list[index].size.text() == "" or classroom_list[index].computer.text() == "":
            return False
    return True


def check_lesson_data(lesson_list):
    if len(lesson_list) == 1:
        return False
    for index in range(1, len(lesson_list)):
        if lesson_list[index].teacher.currentIndex() == 0 or lesson_list[index].group.currentIndex() == 0 or lesson_list[index].lesson.text() == "" or lesson_list[index].quantity.text() == "":
            return False
    return True
