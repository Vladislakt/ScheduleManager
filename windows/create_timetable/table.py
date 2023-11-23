from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QScrollArea, \
    QVBoxLayout, QComboBox

from DataBase.get_list_from_db import getLessonsByGroup, getGroupNameList
from DataBase.select_queries import getTeacherName
from horizontal_line import QHLine
from vertical_line import QVLine
from windows.create_timetable.modified_combobox import ModifiedQComboBox

db = "test"

groups = getGroupNameList(db)


def get_data_from_database():
    courses = []
    for group in groups:
        lessons = getLessonsByGroup(db, group)
        courses_for_one_group = []
        for i in range(len(lessons)):
            courses_for_one_group.append(f"{lessons[i].lesson_name} ({getTeacherName(db, lessons[i].teach_id)})")
        courses.append(courses_for_one_group)
    return courses


class Table(QWidget):
    def __init__(self, days, number_of_classes_per_day):
        super().__init__()
        # self.setStyleSheet("background-color: rgb(255,200,0); ")
        self.columns_width = 300
        self.courses = get_data_from_database()
        self.groups = groups
        self.len_groups = len(self.groups)
        self.days = days
        self.len_days = len(self.days)
        self.number_of_classes_per_day = number_of_classes_per_day
        self.courses_comboboxes = [['' for _ in range(self.len_groups)]
                                   for _ in range(self.len_days * number_of_classes_per_day)]
        self.scroll_area_widget = QWidget()
        self.scroll_area_layout = QGridLayout()
        self.main_layout = QVBoxLayout()
        self.add_scroll_area()
        self.setLayout(self.main_layout)

    def add_scroll_area(self):
        scroll_area = QScrollArea()
        self.create_table()
        self.scroll_area_widget.setLayout(self.scroll_area_layout)
        scroll_area.setWidget(self.scroll_area_widget)
        self.main_layout.addWidget(scroll_area)

    def create_table(self):
        for i in range(self.len_groups):
            for j in range(self.len_days):
                for k in range(self.number_of_classes_per_day):
                    self.add_days(j)
                    self.add_number_of_classes(j, k)
                    self.add_groups(i)
                    self.add_course_choice(i, j, k)
                    self.add_classroom_choise(i, j, k)
                    self.add_horizontal_lines(j)
                    self.add_vertical_lines(i)
                    self.connect_to_courses_comboboxes(i, j, k)

    def add_days(self, j):
        day = QLabel(self.days[j])
        self.scroll_area_layout.addWidget(day, 2 + j * (self.number_of_classes_per_day + 1), 0,
                                          self.number_of_classes_per_day, 1)

    def add_number_of_classes(self, j, k):
        label = QLabel(str(k + 1))
        self.scroll_area_layout.addWidget(label, 2 + j * (self.number_of_classes_per_day + 1) + k, 1, 1, 1)

    def add_groups(self, i):
        group_name = QLabel(self.groups[i])
        group_name.setFixedWidth(self.columns_width)
        group_name.setAlignment(Qt.AlignCenter)
        self.scroll_area_layout.addWidget(group_name, 0, 3 + i * 3, 1, 2)

    def add_course_choice(self, i, j, k):
        course = ModifiedQComboBox(2 + j * (self.number_of_classes_per_day + 1) + k, 3 + i * 3, self.scroll_area_widget)
        course.addItem("")
        course.addItems(self.courses[i])
        course.view().setMinimumWidth(400)
        course.setFixedWidth(self.columns_width - 50)
        self.scroll_area_layout.addWidget(course, 2 + j * (self.number_of_classes_per_day + 1) + k,
                                          3 + i * 3, 1, 1)

    def connect_to_courses_comboboxes(self, i, j, k):
        course_combobox = self.scroll_area_layout.itemAtPosition(2 + j * (self.number_of_classes_per_day + 1) + k,
                                                                 3 + i * 3).widget()
        course_combobox.currentTextChanged.connect(lambda: self.check_lessons_in_row(course_combobox.get_row()))

    def check_lessons_in_row(self, row):
        teacher_ids = []
        for i in range(self.len_groups):
            self.scroll_area_layout.itemAtPosition(row, 3 + i * 3). \
                widget().setStyleSheet("background-color: rgb(255,255,255); ")
        for i in range(self.len_groups):
            current_index = self.scroll_area_layout.itemAtPosition(row, 3 + i * 3).widget().currentIndex()-1
            lessons = getLessonsByGroup(db, groups[i])
            if current_index >= 0:
                id = lessons[current_index].teach_id
            else:
                id = 0
                teacher_ids.append(id)
                continue
            if id in teacher_ids:
                teacher_ids.append(id)
                same_teacher = teacher_ids.index(id)
                self.scroll_area_layout.itemAtPosition(row, 3 + same_teacher * 3). \
                    widget().setStyleSheet("background-color: rgb(255,76,91); ")
                self.scroll_area_layout.itemAtPosition(row, 3 + i * 3). \
                    widget().setStyleSheet("background-color: rgb(255,76,91); ")
            else:
                teacher_ids.append(id)

    def add_classroom_choise(self, i, j, k):
        classroom = QComboBox()
        classroom.setFixedWidth(50)
        self.scroll_area_layout.addWidget(classroom, 2 + j * (self.number_of_classes_per_day + 1) + k,
                                          4 + i * 3, 1, 1)

    def add_horizontal_lines(self, j):
        horizontal_line = QHLine()
        self.scroll_area_layout.addWidget(horizontal_line, 1 + j * (self.number_of_classes_per_day + 1), 0, 1,
                                          3 + self.len_groups * 3)

    def add_vertical_lines(self, i):
        vertical_line = QVLine()
        self.scroll_area_layout.addWidget(vertical_line, 0, 2 + i * 3,
                                          self.len_days * (self.number_of_classes_per_day + 1) + 1, 1)
