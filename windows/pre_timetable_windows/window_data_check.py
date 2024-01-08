def check_new_bd_name(new_name):
    return new_name != ""


def check_teachers_data(teacher_list):
    for index in range(1, len(teacher_list)):
        if teacher_list[index].teacher.text() == "":
            return False
    return True


def check_groups_data(group_list):
    for index in range(1, len(group_list)):
        if group_list[index].group.text() == "" or group_list[index].size.text() == "":
            return False
    return True


def check_classrooms_data(classroom_list):
    for index in range(1, len(classroom_list)):
        if classroom_list[index].classroom.text() == "" or classroom_list[index].size.text() == "" or classroom_list[index].computer.text() == "":
            return False
    return True
