from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout


class Buttons(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignRight)
        save = QPushButton("Сохранить")
        to_db = QPushButton("К БД")
        exit = QPushButton("Выход")
        layout.addWidget(save)
        layout.addWidget(to_db)
        layout.addWidget(exit)
        self.setLayout(layout)
