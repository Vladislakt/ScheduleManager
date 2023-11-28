from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QScrollArea, QVBoxLayout

from horizontal_line import QHLine
from vertical_line import QVLine
from modified_combobox import ModifiedQComboBox
from operations_with_database import get_group_names, get_courses, get_courses_with_teachers, get_classrooms
from table_check import check_teachers_in_row, check_classrooms_in_row, stylesheet


class Table(QWidget):
    def __init__(self, db, days, number_of_classes_per_day):
        super().__init__()
        self.columns_width = 300

        self.group_names = get_group_names(db)
        self.courses_with_teachers = get_courses_with_teachers(db)
        self.classrooms = get_classrooms(db)
        self.courses = get_courses(db)

        self.days = days
        self.number_of_classes_per_day = number_of_classes_per_day
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
        for i in range(len(self.group_names)):
            for j in range(len(self.days)):
                for k in range(self.number_of_classes_per_day):
                    self.add_days(j)
                    self.add_number_of_classes(j, k)
                    self.add_groups(i)
                    self.add_course_choice(i, j, k)
                    self.add_classroom_choise(i, j, k)
                    self.add_horizontal_lines(j)
                    self.add_vertical_lines(i)
                    self.connect_to_courses_comboboxes(i, j, k)
                    self.connect_to_classroom_comboboxes(i, j, k)

    def add_days(self, j):
        day = QLabel(self.days[j])
        self.scroll_area_layout.addWidget(day, 2 + j * (self.number_of_classes_per_day + 1), 0,
                                          self.number_of_classes_per_day, 1)

    def add_number_of_classes(self, j, k):
        label = QLabel(str(k + 1))
        self.scroll_area_layout.addWidget(label, 2 + j * (self.number_of_classes_per_day + 1) + k, 1, 1, 1)

    def add_groups(self, i):
        group_name = QLabel(self.group_names[i])
        group_name.setFixedWidth(self.columns_width)
        group_name.setAlignment(Qt.AlignCenter)
        self.scroll_area_layout.addWidget(group_name, 0, 3 + i * 3, 1, 2)

    def add_course_choice(self, i, j, k):
        course = ModifiedQComboBox(2 + j * (self.number_of_classes_per_day + 1) + k, 3 + i * 3, self.scroll_area_widget)
        course.setObjectName("regular")
        course.setStyleSheet(stylesheet)
        course.setPlaceholderText("Предмет")
        course.addItem("")
        course.addItems(self.courses_with_teachers[i])
        course.view().setMinimumWidth(415)
        course.setFixedWidth(self.columns_width - 50)
        self.scroll_area_layout.addWidget(course, 2 + j * (self.number_of_classes_per_day + 1) + k, 3 + i * 3, 1, 1)

    def connect_to_courses_comboboxes(self, i, j, k):
        course_combobox = self.scroll_area_layout.itemAtPosition(2 + j * (self.number_of_classes_per_day + 1) + k,
                                                                 3 + i * 3).widget()
        course_combobox.currentTextChanged.connect(
            lambda: check_teachers_in_row(self.scroll_area_layout, course_combobox.get_row(), self.group_names,
                                          self.courses))

    def add_classroom_choise(self, i, j, k):
        classroom = ModifiedQComboBox(
            2 + j * (self.number_of_classes_per_day + 1) + k, 4 + i * 3, self.scroll_area_widget)
        classroom.setObjectName("regular")
        classroom.setStyleSheet(stylesheet)
        classroom.setPlaceholderText("Кабинет")
        classroom.setFixedWidth(65)
        classroom.addItem("")
        for c in range(len(self.classrooms)):
            classroom.addItem(self.classrooms[c].class_number)
        self.scroll_area_layout.addWidget(classroom, 2 + j * (self.number_of_classes_per_day + 1) + k,
                                          4 + i * 3, 1, 1)

    def connect_to_classroom_comboboxes(self, i, j, k):
        classroom_combobox = self.scroll_area_layout.itemAtPosition(2 + j * (self.number_of_classes_per_day + 1) + k,
                                                                    4 + i * 3).widget()
        classroom_combobox.currentTextChanged.connect(
            lambda: check_classrooms_in_row(self.scroll_area_layout, classroom_combobox.get_row(), self.group_names))

    def add_horizontal_lines(self, j):
        horizontal_line = QHLine()
        self.scroll_area_layout.addWidget(horizontal_line, 1 + j * (self.number_of_classes_per_day + 1), 0, 1,
                                          3 + len(self.group_names) * 3)

    def add_vertical_lines(self, i):
        vertical_line = QVLine()
        self.scroll_area_layout.addWidget(vertical_line, 0, 2 + i * 3,
                                          len(self.days) * (self.number_of_classes_per_day + 1) + 1, 1)
