stylesheet = open("stylesheet.qss").read()


def check_teachers_in_row(scroll_area_layout, row, group_names, courses):
    teacher_id_list = []
    for i in range(len(group_names)):
        scroll_area_layout.itemAtPosition(row, 3 + i * 3).widget().setObjectName("regular")
        scroll_area_layout.itemAtPosition(row, 3 + i * 3).widget().setStyleSheet(stylesheet)
    for i in range(len(group_names)):
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
            scroll_area_layout.itemAtPosition(row, 3 + same_teacher * 3).widget().setObjectName("highlighted-course")
            scroll_area_layout.itemAtPosition(row, 3 + same_teacher * 3).widget().setStyleSheet(stylesheet)
            scroll_area_layout.itemAtPosition(row, 3 + i * 3).widget().setObjectName("highlighted-course")
            scroll_area_layout.itemAtPosition(row, 3 + i * 3).widget().setStyleSheet(stylesheet)
        else:
            teacher_id_list.append(teacher_id)


def check_classrooms_in_row(scroll_area_layout, row, group_names):
    classroom_list = []
    for i in range(len(group_names)):
        scroll_area_layout.itemAtPosition(row, 4 + i * 3).widget().setObjectName("regular")
        scroll_area_layout.itemAtPosition(row, 4 + i * 3).widget().setStyleSheet(stylesheet)
    for i in range(len(group_names)):
        classroom = scroll_area_layout.itemAtPosition(row, 4 + i * 3).widget().currentText()
        if classroom == "":
            classroom_list.append(classroom)
            continue
        if classroom in classroom_list:
            classroom_list.append(classroom)
            same_classroom = classroom_list.index(classroom)
            scroll_area_layout.itemAtPosition(row, 4 + same_classroom * 3).widget().\
                setObjectName("highlighted-classroom")
            scroll_area_layout.itemAtPosition(row, 4 + same_classroom * 3).widget().setStyleSheet(stylesheet)
            scroll_area_layout.itemAtPosition(row, 4 + i * 3).widget().setObjectName("highlighted-classroom")
            scroll_area_layout.itemAtPosition(row, 4 + i * 3).widget().setStyleSheet(stylesheet)
        else:
            classroom_list.append(classroom)
