from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

from database.save_functions import save_information
from database.select_queries import getIsSaturday, getMaxLesson
from windows.create_timetable_window.timetable_window import TimetableWindow


class AddInformationWindow(QMainWindow):
    def __init__(self, pre_window, current_database):
        super().__init__()

        # Создание объекта предыдущего окна
        self.pre_window = pre_window
        self.current_database = current_database

        # Настройка окна
        self.setFixedSize(1280, 720)
        self.setWindowTitle("OOO Knopocnie Kabanchiki 3C++")

        label = QLabel("Добавьте дополнительную информацию")

        label.setStyleSheet("color: white")

        id = QFontDatabase.addApplicationFont("Fonts/RobotoSlab.ttf")
        families = QFontDatabase.applicationFontFamilies(id)

        label.setFont(QFont(families, 20))

        label.setAlignment(Qt.AlignCenter)

        # "Сколько сгенерирова максимум возможно пар"
        widget_slider = QWidget()
        layout_slider = QVBoxLayout()
        self.max_leson = QSlider(Qt.Orientation.Horizontal, self)
        self.max_leson.setRange(1, 10)
        self.max_leson.setTickPosition(QSlider.TicksBelow)
        self.max_leson.setFixedSize(500, 100)
        label_slider = QLabel("Максимум пар в день: 1")
        label_slider.setObjectName("baseText")
        self.max_leson.valueChanged.connect(lambda value:
                                       label_slider.setText(f"Максимум пар в день: {value}"))

        self.max_leson.setValue(getMaxLesson(self.current_database))
        label_slider.setText(f"Максимум пар в день: {getMaxLesson(self.current_database)}")

        layout_slider.addWidget(self.max_leson)
        layout_slider.addWidget(label_slider)

        widget_slider.setLayout(layout_slider)

        # Чекбокс для субботы
        self.saturday = QCheckBox("Убрать субботу из расписания")
        self.saturday.setObjectName("saturday")

        self.saturday.setChecked(getIsSaturday(self.current_database))

        layout_slider.addWidget(self.saturday)
        layout_slider.setAlignment(Qt.AlignCenter)

        # кнопки
        widget_button = QWidget()

        button_back = QPushButton("Назад")
        button_back.setObjectName("switching")
        button_back.setFont(QFont('Times', 10))
        button_back.setFixedSize(120, 45)

        button_back.clicked.connect(self.openPreWindow)

        kostil1 = QLabel()
        kostil2 = QLabel()
        button_next = QPushButton("Далее")
        button_next.setObjectName("switching")
        button_next.setFont(QFont('Times', 10))
        button_next.setFixedSize(120, 45)

        button_next.clicked.connect(self.openTimetableWindow)

        buttonLayout = QGridLayout()

        buttonLayout.addWidget(button_back, 0, 0)
        buttonLayout.addWidget(kostil1, 0, 1)
        buttonLayout.addWidget(kostil2, 0, 2)
        buttonLayout.addWidget(button_next, 0, 3)

        buttonLayout.setAlignment(Qt.AlignBottom)
        widget_button.setLayout(buttonLayout)

        # Создаю main widget
        mainWidget = QWidget()

        # Создаю main layout
        mainLayout = QVBoxLayout()

        mainLayout.addWidget(label)
        mainLayout.addWidget(widget_slider)
        # mainLayout.addWidget(saturday)
        mainLayout.addWidget(widget_button)

        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

    def openPreWindow(self):
        self.pre_window.show()
        self.destroy()

    def openTimetableWindow(self):
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
        if self.saturday.isChecked():
            days.remove("Суббота")
        number_of_classes_per_day = self.max_leson.value()

        save_information(self.current_database, self.saturday.isChecked(), number_of_classes_per_day)

        self.new_window = TimetableWindow(self.current_database, days, number_of_classes_per_day, self)
        self.new_window.showMaximized()
        self.close()
