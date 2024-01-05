from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from database.save_functions import save_lessons
from windows.pre_timetable_windows.add_widgets.add_lesson_widget import AddLessonWidget
# from windows.pre_timetable_windows.add_information_window import AddInformationWindow


class AddLessonWindow(QMainWindow):
    def __init__(self, pre_window, current_database):
        super().__init__()

        # Создание объекта предыдущего окна
        self.pre_window = pre_window
        self.current_database = current_database

        # Настройка окна
        self.setFixedSize(1280, 720)
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
        widget_label_layout = QVBoxLayout()

        # Запихиваем layout наверх
        # widget_label_layout.setAlignment(Qt.AlignTop)
        # Создаём label
        label = QLabel("Сопоставьте преподавателей и группы")
        label.setStyleSheet("color: white")

        id = QFontDatabase.addApplicationFont("Fonts/RobotoSlab.ttf")
        families = QFontDatabase.applicationFontFamilies(id)

        label.setFont(QFont(families, 20))
        # Центрую label
        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

        # Запихиваем в layout label
        widget_label_layout.addWidget(label)

        # Задаём виджету layout
        widget_label.setLayout(widget_label_layout)

        # 2)

        # В патерн записываем функция добавления
        self.pattern = AddLessonWidget(current_database)

        # widget_add = self.pattern
        # widget_add_layout = QHBoxLayout()
        # widget_add_layout.setAlignment(Qt.AlignHCenter)
        widget_label_layout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        widget_label_layout.addWidget(self.pattern)
        # 3)
        widget_button = QWidget()

        # Создание мэйнового виджета в который запихиваем 3 виджета (делим всё окно на 3 области) и сразу же layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Создаю кнопки и задаю размер
        # Кнопка назад
        button_back = QPushButton("Назад")
        button_back.setObjectName("switching")
        button_back.setFixedSize(120, 45)
        button_back.setFont(QFont('Times', 10))
        # Кнопка далее
        button_next = QPushButton("Далее")
        button_next.setObjectName("switching")
        button_next.setFixedSize(120, 45)
        button_next.setFont(QFont('Times', 10))

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
        # main_layout.addWidget(widget_add)
        main_layout.addWidget(widget_button)

        # Добавляем layout
        main_widget.setLayout(main_layout)

        # Отображаем главный виджет
        self.setCentralWidget(main_widget)

        # Функционал кнопок

        # При нажатии кнопки назад -> Возвращает на окно заполнения учебных групп и закрывает это окно
        # button_back.clicked.connect(self.openPreWindow)

        # При нажатии кнопки создать -> Открывает окно заполнения классов и закрывает это окно
        # button_next.clicked.connect(self.openInformationWindow)

    # Открытие окна заполнения учебных групп (предыдущее окно)
    # def openPreWindow(self):
    #     self.pre_window.showMaximized()
    #     self.destroy()
    #
    # def openInformationWindow(self):
    #     save_lessons(self.current_database, self.pattern.data_masive, self.pattern.id_massive)
    #     self.new_window = AddInformationWindow(self, self.current_database)
    #     self.new_window.showMaximized()
    #     self.close()
