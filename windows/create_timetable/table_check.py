from windows.create_timetable.operations_with_database import courses


def check_teachers_in_row(scroll_area_layout, row, len_groups):
    teacher_ids = []
    for i in range(len_groups):
        scroll_area_layout.itemAtPosition(row, 3 + i * 3). \
            widget().setStyleSheet("background-color: rgb(255,255,255); ")
    for i in range(len_groups):
        current_index = scroll_area_layout.itemAtPosition(row, 3 + i * 3).widget().currentIndex() - 1
        lessons_one_group = courses[i]
        if current_index >= 0:
            id = lessons_one_group[current_index].teach_id
        else:
            id = 0
            teacher_ids.append(id)
            continue
        if id in teacher_ids:
            teacher_ids.append(id)
            same_teacher = teacher_ids.index(id)
            scroll_area_layout.itemAtPosition(row, 3 + same_teacher * 3). \
                widget().setStyleSheet("background-color: rgb(255,76,91); ")
            scroll_area_layout.itemAtPosition(row, 3 + i * 3). \
                widget().setStyleSheet("background-color: rgb(255,76,91); ")
        else:
            teacher_ids.append(id)


def check_classrooms_in_row(scroll_area_layout, row, len_groups):
    print("ok")
