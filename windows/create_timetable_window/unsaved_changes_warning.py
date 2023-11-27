from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QApplication


class UnsavedChangesWarning(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Сохранить?")
        self.setFixedSize(320, 90)
        layout = QGridLayout()
        question = QLabel("У вас есть несохранённые изменения. Сохранить их?")
        save = QPushButton("Сохранить")
        dont_save = QPushButton("Не сохранять")
        layout.addWidget(question, 0, 0, 1, 2)
        layout.addWidget(save, 1, 0, 1, 1)
        layout.addWidget(dont_save, 1, 1, 1, 1)
        self.setLayout(layout)
