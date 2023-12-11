from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

# from windows.create_timetable_window.timetable_window import TimetableWindow


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
        widget_slider = QWidget()
        layout_slider = QVBoxLayout()
        max_leson = QSlider(Qt.Orientation.Horizontal, self)
        max_leson.setRange(1, 10)
        max_leson.setTickPosition(QSlider.TicksBelow)
        max_leson.setFixedSize(500, 100)

        label_slider = QLabel()
        max_leson.valueChanged.connect(lambda value:
                                            label_slider.setText(f"Максимум пар в день: {value}"))

        layout_slider.addWidget(max_leson)
        layout_slider.addWidget(label_slider)

        widget_slider.setLayout(layout_slider)

        # Чекбокс для субботы
        saturday = QCheckBox("Убрать субботу из расписания")

        # кнопки
        widget_button = QWidget()

        button_back = QPushButton("Назад")

        # button_back.clicked.connect(self.openPreWindow)

        kostil1 = QLabel()
        kostil2 = QLabel()
        button_next = QPushButton("Перейти к созданию расписания")

        # button_next.clicked.connect(self.openTimetableWindow)

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
        mainLayout = QGridLayout()

        mainLayout.addWidget(widget_slider, 0, 0)
        mainLayout.addWidget(saturday, 0, 1)
        mainLayout.addWidget(widget_button)

        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

    # def openPreWindow(self):
    #     self.pre_window.showMaximized()
    #     self.destroy()
    #
    # def openTimetableWindow(self):
    #     days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    #     if self.saturday.isChecked():
    #         days.remove("Суббота")
    #     number_of_classes_per_day = self.max_leson.value()
    #     self.new_window = TimetableWindow(self.current_database, days, number_of_classes_per_day)
    #     self.new_window.showMaximized()
    #     self.close()
