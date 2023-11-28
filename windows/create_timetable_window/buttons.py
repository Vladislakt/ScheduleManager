from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout

from write_xlsx import fill_xlsx


class Buttons(QWidget):
    def __init__(self, table, days, number_of_classes_per_day):
        super().__init__()
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignRight)
        save = QPushButton("Сохранить")
        save.clicked.connect(lambda: fill_xlsx(table, days, number_of_classes_per_day))
        to_db = QPushButton("К БД")
        exit = QPushButton("Выход")
        layout.addWidget(save)
        layout.addWidget(to_db)
        layout.addWidget(exit)
        self.setLayout(layout)
