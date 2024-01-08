def check_new_bd_name(new_name):
    return new_name != ""


def check_teachers_data(teacher_list):
    for line in teacher_list:
        if line.teacher.text() == "":
            return False
    return True


def check_groups_data(group_list):
    for line in group_list:
        if line.group.text() == "" or line.size.text() == "":
            return False
    return True
