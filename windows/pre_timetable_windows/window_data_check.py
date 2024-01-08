def check_new_bd_name(new_name):
    return new_name != ""


def check_teachers_data(teacher_list):
    for line in teacher_list:
        if line.teacher.text() == "":
            return False
    return True
