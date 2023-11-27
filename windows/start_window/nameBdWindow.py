from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

# Окно создания БД с выбором (создать своё бд / импортировать существующее)
class NameBdWindow(QMainWindow):
    def __init__(self, pre_window):
        super().__init__()

        # Создание объекта предыдущего окна
        self.pre_window = pre_window

        # Настройка окна
        self.setMinimumHeight(800)
        self.setMinimumWidth(900)
        self.setWindowTitle("OOO Knopocnie Kabanchiki 3C++")

        # Создаю окно для ввода названия бд
        widget_name_bd = QWidget()
        nameBd = QTextEdit("Введите название расписания")
        nameBd.setFixedSize(500, 50)
        layout_nameBd = QHBoxLayout()
        layout_nameBd.addWidget(nameBd)
        layout_nameBd.setAlignment(Qt.AlignVCenter)
        layout_nameBd.setAlignment(Qt.AlignHCenter)
        widget_name_bd.setLayout(layout_nameBd)

        # Создаю кнопки Далее и назад

        widget_buttons = QWidget()

        button_back = QPushButton("назад")
        button_back.setObjectName("baseButton")
        kostil1 = QLabel()
        kostil2 = QLabel()
        button_next = QPushButton("далее")
        button_next.setObjectName("baseButton")

        button_layout = QGridLayout()
        button_layout.addWidget(button_back, 0, 0)
        button_layout.addWidget(kostil1, 0, 1)
        button_layout.addWidget(kostil2, 0, 2)
        button_layout.addWidget(button_next, 0, 3)

        button_layout.setAlignment(Qt.AlignBottom)

        widget_buttons.setLayout(button_layout)

        # # Подключаю функции открытия окон
        # button_back.clicked.connect(self.pre_window)
        # button_next.clicked.connect(self.open_triple_window)

        # Создаю main widget
        mainWidget = QWidget()
        # Создаю main layout
        mainLayot = QVBoxLayout()
        mainLayot.addWidget(widget_name_bd)
        mainLayot.addWidget(widget_buttons)
        mainWidget.setLayout(mainLayot)

        button_back.clicked.connect(self.open_start_window)
        button_next.clicked.connect(self.open_triple_window)

        self.setCentralWidget(mainWidget)

    # Открытие стартового окна (предыдущее окно)
    def open_start_window(self):
        self.pre_window.showMaximized()
        self.close()

    # Открытие окна заполнения с тремя виджетами
    def open_triple_window(self):
        from addTripleWindow import AddTripleWindow
        self.openTripleWindow = AddTripleWindow(self)
        self.openTripleWindow.showMaximized()
        self.close()
