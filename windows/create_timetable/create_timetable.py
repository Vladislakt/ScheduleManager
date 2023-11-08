from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout

from buttons import Buttons
from table import Table
from courses import Courses
from vertical_line import QVLine


class CreateTimetable(QWidget):
    def __init__(self, courses, groups, days, number_of_classes_per_day):
        super().__init__()
        self.setWindowTitle("Составление расписания")
        self.setBaseSize(1024, 768)
        self.table = Table(groups, days, number_of_classes_per_day)
        self.vertical_line = QVLine()
        self.courses = Courses(courses)
        self.courses.setFixedWidth(300)
        self.buttons = Buttons()
        layout = QHBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.vertical_line)
        layout.addWidget(self.courses)
        layout.setAlignment(Qt.AlignRight)
        self.setLayout(layout)
