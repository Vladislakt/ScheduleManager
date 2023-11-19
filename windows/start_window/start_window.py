from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys


# Стартовое окно
class Start_window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройка окна
        self.setMinimumHeight(800)
        self.setMinimumWidth(900)
        self.setStyleSheet("background-color: #876C99;")
        self.setWindowTitle("OOO Knopocnie Kabanchiki 3C++")

        # Кнопки в окне
        button_create = QPushButton("Создать")
        button_create.setObjectName("baseButton")
        button_edit = QPushButton("Редактировать")
        button_edit.setObjectName("baseButton")
        button_exit = QPushButton("Выйти")
        button_exit.setObjectName("baseButton")

        # Стиль кнопок
        button_create.setFont(QFont("Georgia", 40))
        button_create.setStyleSheet("background-color: #543964;")

        button_edit.setFont(QFont("Georgia", 40))
        button_edit.setStyleSheet("background-color: #543964;")

        button_exit.setFont(QFont("Georgia", 40))
        button_exit.setStyleSheet("background-color: #543964;")

        # Размер кнопок
        button_create.setMinimumSize(350, 100)
        button_edit.setMinimumSize(350, 100)
        button_exit.setMinimumSize(200, 100)

        layout = QGridLayout()

        # Устанавливаем кнопки с помощью сетки
        layout.addWidget(button_create, 0, 0, 1, 2)
        layout.addWidget(button_edit, 0, 2, 1, 2)
        layout.addWidget(button_exit, 1, 1, 1, 2)

        # Центруем кнопки
        layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        # При нажатии кнопки выход -> закрывается приложение
        button_exit.clicked.connect(self.close)

        # При нажатии кнопки создать -> Скрывается это окно -> Переходит на окно создания
        button_create.clicked.connect(self.open_create_start_window)

    def open_create_start_window(self):
        from create_start_window import Create_start_window
        self.switch_create_start_window = Create_start_window(self)
        self.switch_create_start_window.showMaximized()
        self.close()
