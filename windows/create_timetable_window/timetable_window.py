from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout

from buttons import Buttons
from table import Table


class TimetableWindow(QWidget):
    def __init__(self, db, days, number_of_classes_per_day):
        super().__init__()
        self.setWindowTitle("Составление расписания")
        self.table = Table(db, days, number_of_classes_per_day)
        self.buttons = Buttons(self.table, days, number_of_classes_per_day)
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.buttons)
        layout.setAlignment(Qt.AlignRight)
        self.setLayout(layout)
