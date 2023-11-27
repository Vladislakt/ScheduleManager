from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys


# Окно создания БД с выбором (создать своё бд / импортировать существующее)
class Create_start_window(QMainWindow):
    def __init__(self, pre_window):
        super().__init__()

        # Создание объекта предыдущего окна
        self.pre_window = pre_window

        # Настройка окна
        self.setMinimumHeight(800)
        self.setMinimumWidth(900)
        self.setWindowTitle("OOO Knopocnie Kabanchiki 3C++")

        # Кнопки в окне
        button_create_bd = QPushButton("Создать расписание")
        button_create_bd.setObjectName("baseButton")
        button_import_my_bd = QPushButton("Импортировать расписание")
        button_import_my_bd.setObjectName("baseButton")
        button_back = QPushButton("Назад в главное меню")
        button_back.setObjectName("baseButton")

        # Стиль кнопок
        button_create_bd.setFont(QFont("Georgia", 40))

        button_import_my_bd.setFont(QFont("Georgia", 40))

        button_back.setFont(QFont("Georgia", 40))

        # Размер кнопок
        button_create_bd.setMinimumSize(350, 100)
        button_import_my_bd.setMinimumSize(350, 100)
        button_back.setMinimumSize(350, 100)

        # Размещаем кнопки по вертикали
        layout = QVBoxLayout()

        layout.addWidget(button_create_bd)
        layout.addWidget(button_import_my_bd)
        layout.addWidget(button_back)

        # Центруем кнопки
        layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        # Функционал кнопок

        # При нажатии кнопки назад -> Возвращает на стартовое окно и закрывает это окно
        button_back.clicked.connect(self.open_start_window)

        # При нажатии кнопки создать -> Открывает окно заполнения преподавателей и закрывает это окно
        button_create_bd.clicked.connect(self.open_add_teacher)

    # Открытие стартового окна (предыдущее окно)
    def open_start_window(self):
        self.pre_window.showMaximized()
        self.close()

    # Открытие окна заполнение преподавателей (следующее окно)
    def open_add_teacher(self):
        from addTripleWindow import AddTeacher
        self.addTeacher = AddTeacher(self)
        self.addTeacher.showMaximized()
        self.close()

