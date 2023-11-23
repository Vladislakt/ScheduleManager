from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from windows.other_windows.addteacherwidget import AddingTeacherWidget


class Shablon_zapolnenia(QMainWindow):
    def __init__(self, name = "преподователей"):
        super().__init__()

        # Настройка окна
        self.setMinimumSize(900, 800)
        self.setStyleSheet("background-color: #90ee90;")
        self.setWindowTitle("OOO Knopocnie Kabanchiki 3C++")

        # Виджет под кнопки
        widget1 = QWidget()

        pattern = AddingTeacherWidget()

        widget2 = QScrollArea()
        widget2.setWidget(pattern)
        widget2.setWidgetResizable(True)

        widget2.setMinimumSize(500, 500)


        widget2.setStyleSheet("background-color: #f5f5f5;")

        widget3 = QWidget()

        main_widget = QWidget()
        main_layout = QVBoxLayout()


        # Кнопка перехода назад
        button_back = QPushButton("Назад")
        # Кнопка перехода далее
        button_next = QPushButton("Далее")

        # Стиль кнопки
        button_back.setFont(QFont("Georgia", 20))
        button_back.setStyleSheet("background-color: #8B4513;")
        button_next.setFont(QFont("Georgia", 20))
        button_next.setStyleSheet("background-color: #8B4513;")

        # Размер кнопки
        button_back.setFixedSize(120, 50)
        button_next.setFixedSize(120, 50)

        widget3_layout = QGridLayout()

        # Костыли между кнопками (чтобы было расстояние между кнопками)
        kostil1 = QLabel(" ")
        kostil2 = QLabel(" ")

        # С помощью сетки задаём расположение кнопкам
        widget3_layout.addWidget(button_back, 1, 0)
        widget3_layout.addWidget(kostil1, 1, 1)
        widget3_layout.addWidget(kostil2, 1, 2)
        widget3_layout.addWidget(button_next, 1, 3)

        widget3_layout.setAlignment(Qt.AlignBottom)

        widget3.setLayout(widget3_layout)

        widget1_layout = QHBoxLayout()
        widget1_layout.setAlignment(Qt.AlignTop)

        label = QLabel(f"Введите {name}")

        #Стиль текста вверху
        label.setFont(QFont("Georgia", 20))
        label.setAlignment(Qt.AlignCenter)

        widget1_layout.addWidget(label)
        widget1.setLayout(widget1_layout)

        main_layout.addWidget(widget1)
        main_layout.addWidget(widget2)
        main_layout.addWidget(widget3)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


app = QApplication([])
app.setStyleSheet(Path('style.qss').read_text())
window = Shablon_zapolnenia()
window.show()
app.exec()
