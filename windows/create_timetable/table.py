from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QScrollArea, \
    QVBoxLayout, QComboBox

from horizontal_line import QHLine
from vertical_line import QVLine


class Table(QWidget):
    def __init__(self, groups, days, number_of_classes_per_day):
        super().__init__()
        # self.setStyleSheet("background-color: rgb(255,200,0); ")
        self.groups = groups
        self.days = days
        self.number_of_classes_per_day = number_of_classes_per_day
        scroll_area = QScrollArea()
        self.layout = QGridLayout()
        self.add_days()
        self.add_numbers_of_classes()
        self.add_vertical_lines()
        self.add_horizontal_lines()
        self.add_groups()
        widget = QWidget()
        widget.setLayout(self.layout)
        scroll_area.setWidget(widget)
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(scroll_area)
        self.setLayout(self.main_layout)

    def add_days(self):
        for i in range(len(self.days)):
            day = QLabel(self.days[i])
            self.layout.addWidget(day, 2 + i * (self.number_of_classes_per_day + 1), 0, self.number_of_classes_per_day,
                                  1)

    def add_numbers_of_classes(self):
        for i in range(len(self.days)):
            for j in range(self.number_of_classes_per_day):
                label = QLabel(str(j + 1))
                self.layout.addWidget(label, 2 + i * (self.number_of_classes_per_day + 1) + j, 1, 1, 1)

    def add_groups(self):
        columns_width = 200
        for i in range(len(self.groups)):
            group_name = QLabel(self.groups[i])
            group_name.setFixedWidth(columns_width)
            group_name.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(group_name, 0, 3 + i * 3, 1, 2)
            for j in range(len(self.days)):
                for k in range(self.number_of_classes_per_day):
                    course = QComboBox()
                    course.addItems(["a", "b", "c"])
                    course.setFixedWidth(columns_width - 50)
                    classroom = QComboBox()
                    classroom.setFixedWidth(50)
                    self.layout.addWidget(course, 2 + j * (self.number_of_classes_per_day + 1) + k, 3 + i * 3, 1, 1)
                    self.layout.addWidget(classroom, 2 + j * (self.number_of_classes_per_day + 1) + k, 4 + i * 3, 1, 1)

    def add_horizontal_lines(self):
        for i in range(len(self.days)):
            horizontal_line = QHLine()
            self.layout.addWidget(horizontal_line, 1 + i * (self.number_of_classes_per_day + 1), 0, 1,
                                  3 + len(self.groups) * 3)

    def add_vertical_lines(self):
        for i in range(len(self.groups)):
            vertical_line = QVLine()
            vertical_line.setFixedWidth(30)
            self.layout.addWidget(vertical_line, 0, 2 + i * 3,
                                  len(self.days) * (self.number_of_classes_per_day + 1) + 1, 1)
