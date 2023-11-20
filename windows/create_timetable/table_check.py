from windows.create_timetable.operations_with_database import courses


def check_teachers_in_row(scroll_area_layout, row, len_groups):
    teacher_id_list = []
    for i in range(len_groups):
        scroll_area_layout.itemAtPosition(row, 3 + i * 3). \
            widget().setStyleSheet("background-color: rgb(255,255,255); ")
    for i in range(len_groups):
        current_index = scroll_area_layout.itemAtPosition(row, 3 + i * 3).widget().currentIndex() - 1
        lessons_one_group = courses[i]
        if current_index >= 0:
            teacher_id = lessons_one_group[current_index].teach_id
        else:
            teacher_id = 0
            teacher_id_list.append(teacher_id)
            continue
        if teacher_id in teacher_id_list:
            teacher_id_list.append(teacher_id)
            same_teacher = teacher_id_list.index(teacher_id)
            scroll_area_layout.itemAtPosition(row, 3 + same_teacher * 3). \
                widget().setStyleSheet("background-color: rgb(255,76,91); ")
            scroll_area_layout.itemAtPosition(row, 3 + i * 3). \
                widget().setStyleSheet("background-color: rgb(255,76,91); ")
        else:
            teacher_id_list.append(teacher_id)


def check_classrooms_in_row(scroll_area_layout, row, len_groups):
    classroom_list = []
    for i in range(len_groups):
        scroll_area_layout.itemAtPosition(row, 4 + i * 3). \
            widget().setStyleSheet("background-color: rgb(255,255,255); ")
    for i in range(len_groups):
        classroom = scroll_area_layout.itemAtPosition(row, 4 + i * 3).widget().currentText()
        if classroom == "":
            classroom_list.append(classroom)
            continue
        if classroom in classroom_list:
            classroom_list.append(classroom)
            same_classroom = classroom_list.index(classroom)
            scroll_area_layout.itemAtPosition(row, 4 + same_classroom * 3). \
                widget().setStyleSheet("background-color: rgb(255,76,91); ")
            scroll_area_layout.itemAtPosition(row, 4 + i * 3). \
                widget().setStyleSheet("background-color: rgb(255,76,91); ")
        else:
            classroom_list.append(classroom)
