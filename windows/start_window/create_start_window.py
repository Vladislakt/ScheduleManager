from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys


# Окно создания БД с выбором (создать своё бд / импортировать существующее)
class Create_start_window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройка окна
        self.setMinimumHeight(800)
        self.setMinimumWidth(900)
        self.setStyleSheet("background-color: #287233;")
        self.setWindowTitle("OOO Knopocnie Kabanchiki 3C++")

        # Кнопки в окне
        button_create_bd = QPushButton("Создать расписание")
        button_import_my_bd = QPushButton("Импортировать расписание")
        button_back = QPushButton("Назад в главное меню")

        # Стиль кнопок
        button_create_bd.setFont(QFont("Georgia", 40))
        button_create_bd.setStyleSheet("background-color: #8B4513;")

        button_import_my_bd.setFont(QFont("Georgia", 40))
        button_import_my_bd.setStyleSheet("background-color: #8B4513;")

        button_back.setFont(QFont("Georgia", 40))
        button_back.setStyleSheet("background-color: #8B4513;")

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

        # При нажатии кнопки назад -> Возвращает на стартовое окно и скрывает это окно
        button_back.clicked.connect(self.hide)
        button_back.clicked.connect(self.open_start_window)

        # При нажатии кнопки создать -> Открывает окно заполнения преподавателей и скрывает это окно
        # button_create_bd.clicked.connect(self.hide)
        # button_create_bd.clicked.connect(self.creatorbd)

    def open_start_window(self):
        # self.switch_start_window = Start_window()
        # self.switch_start_window.showMaximized()
        self.hide()



    # def creatorbd(self):
    #     self.switch_creatorbd = CreatBd_teatcher()
    #     self.switch_creatorbd.showMaximized()