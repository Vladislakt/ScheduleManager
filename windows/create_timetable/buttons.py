from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout


class Buttons(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignRight)
        save_button = QPushButton("Сохранить")
        cancel_button = QPushButton("Отмена")
        layout.addWidget(save_button)
        layout.addWidget(cancel_button)
        self.setLayout(layout)
