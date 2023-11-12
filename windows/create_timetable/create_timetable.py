from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout

from buttons import Buttons
from table import Table
from courses import Courses
from vertical_line import QVLine


class CreateTimetable(QWidget):
    def __init__(self, courses, groups, days, number_of_classes_per_day):
        super().__init__()
        self.setWindowTitle("Составление расписания")
        self.table = Table(groups, days, number_of_classes_per_day)
        self.buttons = Buttons()
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.buttons)
        layout.setAlignment(Qt.AlignRight)
        self.setLayout(layout)
