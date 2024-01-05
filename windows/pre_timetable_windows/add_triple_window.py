from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from database.save_functions import save_teachers, save_groups, save_classrooms
from windows.pre_timetable_windows.add_widgets.add_teacher_widget import AddTeacherWidget
from windows.pre_timetable_windows.add_widgets.add_group_widget import AddGroupWidget
from windows.pre_timetable_windows.add_widgets.add_classroom_widget import AddClassroomWidget
# from windows.pre_timetable_windows.add_lesson_window import AddLessonWindow


class AddTripleWindow(QMainWindow):
    def __init__(self, pre_window, current_database):
        super().__init__()

        #Создание объекта предыдущего окна
        self.pre_window = pre_window
        self.current_database = current_database

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

        # Создаём label
        label = QLabel()
        label_teacher = QLabel("Заполните учителей")
        label_group = QLabel("Заполните группы")
        label_classroom = QLabel("Заполните классы")

        id = QFontDatabase.addApplicationFont("Fonts/RobotoSlab.ttf")
        families = QFontDatabase.applicationFontFamilies(id)

        label_teacher.setFont(QFont(families, 20))
        label_group.setFont(QFont(families, 20))
        label_classroom.setFont(QFont(families, 20))

        # Запихиваем в layout label
        widget_label_layout.addWidget(label_teacher)
        widget_label_layout.addWidget(label_group)
        widget_label_layout.addWidget(label_classroom)

        # Центрую label
        label.setAlignment(Qt.AlignCenter)

        # Задаём виджету layout
        widget_label.setLayout(widget_label_layout)

        # 2)

        # В патерн записываем функция добавления
        self.pattern_teacher = AddTeacherWidget(current_database)
        self.pattern_group = AddGroupWidget(current_database)
        self.pattern_classroom = AddClassroomWidget(current_database)

        widget_add = QWidget()
        widget_add_layout = QHBoxLayout()
        widget_add_layout.addWidget(self.pattern_teacher)
        widget_add_layout.addWidget(self.pattern_group)
        widget_add_layout.addWidget(self.pattern_classroom)
        widget_add_layout.setAlignment(Qt.AlignCenter)
        widget_add.setLayout(widget_add_layout)

        # 3)
        widget_button = QWidget()

        # Создание мэйнового виджета в который запихиваем 3 виджета (делим всё окно на 3 области) и сразу же layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Создаю кнопки и задаю размер
        # Кнопка назад
        button_back = QPushButton("На стартовую")
        button_back.setObjectName("baseButton")
        button_back.setFixedSize(120, 50)
        # Кнопка далее
        button_next = QPushButton("Сохранить")
        button_next.setObjectName("baseButton")
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

        main_layout.setAlignment(Qt.AlignHCenter)

        # Отображаем главный виджет
        self.setCentralWidget(main_widget)

        # Функционал кнопок

        # При нажатии кнопки назад -> Открывает стартовое окно создания и закрывает это окно
        # button_back.clicked.connect(self.openPreWindow)
        #
        # При нажатии кнопки далее -> Открывает окно заполнения учебных групп и закрывает это окно
        # button_next.clicked.connect(self.openLessonWindow)

    # Открытие предыдущего окна
    # def openPreWindow(self):
    #     self.pre_window.pre_window.showMaximized()
    #     self.pre_window.destroy()
    #     self.destroy()
    #
    # def openLessonWindow(self):
    #     save_teachers(self.current_database, self.pattern_teacher.data_masive, self.pattern_teacher.id_massive)
    #     save_groups(self.current_database, self.pattern_group.data_masive)
    #     save_classrooms(self.current_database, self.pattern_classroom.data_masive)
    #     self.new_window = AddLessonWindow(self, self.current_database)
    #     self.new_window.showMaximized()
    #     self.close()
