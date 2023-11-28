from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys


class AddInformationWindow(QMainWindow):
    def __init__(self, pre_window, current_database):
        super().__init__()

        # Создание объекта предыдущего окна
        self.pre_window = pre_window
        self.current_database = current_database

        # Настройка окна
        self.setMinimumSize(900, 800)
        self.setWindowTitle("OOO Knopocnie Kabanchiki 3C++")

        # "Сколько сгенерирова максимум возможно пар"
        self.max_leson = QLineEdit("Сколько сгенерирова максимум возможно пар")
        self.max_leson.setFixedSize(500, 100)

        # Чекбокс для субботы
        self.saturday = QCheckBox()

        # кнопки
        widget_button = QWidget()

        button_back = QPushButton("Назад")

        button_back.clicked.connect(self.openPreWindow)

        kostil1 = QLabel()
        kostil2 = QLabel()
        button_next = QPushButton("Перейти к созданию расписания")

        button_next.clicked.connect(self.openTimetableWindow)

        buttonLayout = QGridLayout()

        buttonLayout.addWidget(button_back, 0, 0)
        buttonLayout.addWidget(kostil1, 0, 1)
        buttonLayout.addWidget(kostil2, 0, 2)
        buttonLayout.addWidget(button_next, 0, 3)

        widget_button.setLayout(buttonLayout)

        # Создаю main widget
        mainWidget = QWidget()

        # Создаю main layout
        mainLayout = QVBoxLayout()

        mainLayout.addWidget(self.max_leson)
        mainLayout.addWidget(self.saturday)
        mainLayout.addWidget(widget_button)

        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

    def openPreWindow(self):
        self.pre_window.showMaximized()
        self.destroy()

    def openTimetableWindow(self):
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
        if self.saturday.isChecked():
            days.remove("Суббота")
        number_of_classes_per_day = int(self.max_leson.text())

        # number_of_classes_per_day = 4
        # self.new_window = TimetableWindow(self.current_database, days, number_of_classes_per_day)
        # self.new_window.showMaximized()
        # self.close()
