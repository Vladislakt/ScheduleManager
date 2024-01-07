from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout

from windows.create_timetable_window.buttons import Buttons
from windows.create_timetable_window.table import Table


class TimetableWindow(QWidget):
    def __init__(self, db, days, number_of_classes_per_day, pre_window):
        super().__init__()
        self.pre_window = pre_window
        self.setWindowTitle("Составление расписания")
        self.table = Table(db, days, number_of_classes_per_day)
        self.buttons = Buttons(db, self.table, days, number_of_classes_per_day, self.pre_window, self)
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.buttons)
        layout.setAlignment(Qt.AlignRight)
        self.setLayout(layout)
