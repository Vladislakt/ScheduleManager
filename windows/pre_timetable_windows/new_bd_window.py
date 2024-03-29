from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys


# Хуёво запушилось
# Окно создания БД с выбором (создать своё бд / импортировать существующее)
from database.create_database import create_database
from database.insert_name import insert_name
from database.save_functions import save_information
from windows.pre_timetable_windows.add_triple_window import AddTripleWindow
from windows.pre_timetable_windows.window_data_check import check_new_bd_name


class NewBDWindow(QMainWindow):
    def __init__(self, pre_window):
        super().__init__()

        # Создание объекта предыдущего окна
        self.pre_window = pre_window

        # Настройка окна
        self.setFixedSize(1280, 720)
        self.setWindowTitle("OOO Knopocnie Kabanchiki 3C++")

        # Вступительный лэйбл

        label = QLabel('Введите название нового расписания')

        label.setStyleSheet("color: white")

        id = QFontDatabase.addApplicationFont("windows/pre_timetable_windows/Fonts/RobotoSlab.ttf")
        families = QFontDatabase.applicationFontFamilies(id)

        label.setFont(QFont(families, 40))
        label.setAlignment(Qt.AlignCenter)

        # Создаю окно для ввода названия бд
        widget_name_bd = QWidget()
        self.name_BD = QLineEdit()
        self.name_BD.setPlaceholderText("Введите название таблицы")
        self.name_BD.setFixedSize(500, 50)
        layout_nameBd = QVBoxLayout()
        layout_nameBd.addWidget(self.name_BD)
        layout_nameBd.setAlignment(Qt.AlignCenter)
        widget_name_bd.setLayout(layout_nameBd)

        # Создаю кнопки Далее и назад

        widget_buttons = QWidget()

        button_back = QPushButton("Назад")
        button_back.setObjectName("switching")
        button_back.setFont(QFont('Times', 10))
        kostil1 = QLabel("")
        kostil2 = QLabel("")
        button_next = QPushButton("Далее")
        button_next.setObjectName("switching")
        button_next.setFont(QFont('Times', 10))

        button_back.setFixedSize(120, 45)
        button_next.setFixedSize(120, 45)

        button_layout = QGridLayout()
        button_layout.addWidget(button_back, 0, 0)
        button_layout.addWidget(kostil1, 0, 1)
        button_layout.addWidget(kostil2, 0, 2)
        button_layout.addWidget(button_next, 0, 3)

        button_layout.setAlignment(Qt.AlignBottom)

        widget_buttons.setLayout(button_layout)

        # Подключаю функции открытия окон
        button_back.clicked.connect(self.openPreWindow)
        button_next.clicked.connect(self.openTripleWindow)

        # Создаю main widget
        mainWidget = QWidget()
        # Создаю main layout
        mainLayot = QVBoxLayout()
        mainLayot.addWidget(label)
        mainLayot.addWidget(widget_name_bd)
        mainLayot.addWidget(widget_buttons)
        mainWidget.setLayout(mainLayot)

        self.setCentralWidget(mainWidget)

    def openPreWindow(self):
        self.pre_window.show()
        self.destroy()

    def openTripleWindow(self):
        if check_new_bd_name(self.name_BD.text()):
            new_name = self.name_BD.text()
            current_database = create_database()
            insert_name(current_database, new_name)
            save_information(current_database, False, 1)
            self.pre_window.destroy()
            self.new_window = AddTripleWindow(self, current_database)
            self.new_window.show()
            self.close()
        else:
            warning = QMessageBox()
            warning.setWindowTitle("Ошибка!")
            warning.setText("Название не должно быть пустым!")
            warning.setStandardButtons(QMessageBox.Ok)
            warning.exec()
