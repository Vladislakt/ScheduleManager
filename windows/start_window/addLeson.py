from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from windows.other_windows.addlessonwidget import AddingLessonWidget

class AddLeson(QMainWindow):
    def __init__(self, pre_window):
        super().__init__()

        # Создание объекта предыдущего окна
        self.pre_window = pre_window

        # Настройка окна
        self.setMinimumSize(900, 800)
        self.setWindowTitle("OOO Knopocnie Kabanchiki 3C++")

        # Используемые виджеты
        # 1) Текст сверху
        # 2) Виджет заполнения (плюс размер окна заполнения)
        # 3) Кнопки далее/назад

        # label -> Виджет добавления -> Кнопки
        # 1)

        # Виджет нужен для того, чтобы поделить экран
        widget_label = QWidget()

        # Создаём layout
        widget_label_layout = QHBoxLayout()

        # Запихиваем layout наверх
        widget_label_layout.setAlignment(Qt.AlignTop)
        # Создаём label
        label = QLabel("Сопоставьте преподавателей и группы")

        # Центрую label
        label.setAlignment(Qt.AlignCenter)

        # Запихиваем в layout label
        widget_label_layout.addWidget(label)

        # Задаём виджету layout
        widget_label.setLayout(widget_label_layout)

        # 2)

        # В патерн записываем функция добавления
        pattern = AddingLessonWidget()

        # Добавляем скрол бар
        widget_add = QScrollArea()

        # 3)
        widget_button = QWidget()

        # Создание мэйнового виджета в который запихиваем 3 виджета (делим всё окно на 3 области) и сразу же layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Создаю кнопки и задаю размер
        # Кнопка назад
        button_back = QPushButton("Назад")
        button_back.setFixedSize(120, 50)
        # Кнопка далее
        button_next = QPushButton("Далее")
        button_next.setFixedSize(120, 50)

        # Создаю layout для кнопок

        widget_button_layout = QGridLayout()

        # С помощью сетки размещаем кнопки и запихиваем между кнопками костыли (потом сделаем нормально)

        kostil1 = QLabel(" ")
        kostil2 = QLabel(" ")

        widget_button_layout.addWidget(button_back, 0, 0)
        widget_button_layout.addWidget(kostil1, 0, 1)
        widget_button_layout.addWidget(kostil2, 0, 2)
        widget_button_layout.addWidget(button_next, 0, 3)

        widget_button.setLayout(widget_button_layout)
        # Запихиваем вниз кнопки
        widget_button_layout.setAlignment(Qt.AlignBottom)



        # Добавляем виджеты в главный виджет
        main_layout.addWidget(widget_label)
        main_layout.addWidget(widget_add)
        main_layout.addWidget(widget_button)

        # Добавляем layout
        main_widget.setLayout(main_layout)

        # Отображаем главный виджет
        self.setCentralWidget(main_widget)

        # Функционал кнопок

        # При нажатии кнопки назад -> Возвращает на окно заполнения учебных групп и закрывает это окно
        button_back.clicked.connect(self.open_add_group)

        # При нажатии кнопки создать -> Открывает окно заполнения классов и закрывает это окно
        button_next.clicked.connect(self.open_add_classroom)

    # Открытие окна заполнения учебных групп (предыдущее окно)
    def open_add_group(self):
        self.pre_window.showMaximized()
        self.close()

    # Открытие окна заполнение классов (следующее окно)
    def open_add_classroom(self):
        from addClassroom import AddClassroom
        self.addClassroom = AddClassroom(self)
        self.addClassroom.showMaximized()
        self.close()