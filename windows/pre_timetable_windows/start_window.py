from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# Стартовое окно
from windows.pre_timetable_windows.old_bd_window import EditOldBDWindow
from windows.pre_timetable_windows.new_bd_window import NewBDWindow


class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройка окна
        self.setFixedSize(1280, 720)
        self.setWindowTitle("OOO Knopocnie Kabanchiki 3C++")

        label_widget = QWidget()
        label_name_proga = QLabel("ScheduleManager")
        label_name_company = QLabel("Directed by OOO Knopochnie Kabanchiki")

        id1 = QFontDatabase.addApplicationFont("windows/pre_timetable_windows/Fonts/NanumMyeongjo-Regular.ttf")
        nanum = QFontDatabase.applicationFontFamilies(id1)

        id2 = QFontDatabase.addApplicationFont("windows/pre_timetable_windows/Fonts/Judson-Regular.ttf")
        judson = QFontDatabase.applicationFontFamilies(id2)

        label_name_proga.setFont(QFont(nanum, 41))
        label_name_company.setFont(QFont(judson, 17))
        label_name_proga.setObjectName("baseText")
        label_name_company.setObjectName("baseText")
        label_layout = QVBoxLayout()
        label_layout.addWidget(label_name_proga)
        label_layout.addWidget(label_name_company)
        label_layout.setAlignment(Qt.AlignCenter)

        label_widget.setLayout(label_layout)

        # Кнопки в окне
        button_widget = QWidget()
        button_create = QPushButton("Создать")
        button_create.setObjectName("baseButton")
        button_create.setFont(QFont('Times', 15))
        button_edit = QPushButton("Редактировать")
        button_edit.setObjectName("baseButton")
        button_edit.setFont(QFont('Times', 15))
        button_exit = QPushButton("Выйти")
        button_exit.setObjectName("buttonExit")
        button_exit.setFont(QFont('Times', 15))

        # Размер кнопок
        button_create.setFixedSize(250, 100)
        button_edit.setFixedSize(250, 100)
        button_exit.setFixedSize(250, 100)

        button_layout = QGridLayout()
        kostil = QLabel("")

        # Устанавливаем кнопки с помощью сетки
        button_layout.addWidget(button_create, 0, 0)
        button_layout.addWidget(kostil, 0, 1)
        button_layout.addWidget(button_edit, 0, 2)
        button_layout.addWidget(button_exit, 1, 1)

        # Центруем кнопки
        button_layout.setAlignment(Qt.AlignCenter)

        button_widget.setLayout(button_layout)

        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(label_widget)
        main_layout.addWidget(button_widget)
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

        # При нажатии кнопки выход -> закрывается приложение
        button_exit.clicked.connect(self.close)

        # При нажатии кнопки создать -> Скрывается это окно -> Переходит на окно создания
        button_create.clicked.connect(self.createNewBD)

        button_edit.clicked.connect(self.editOldBD)

    def createNewBD(self):
        self.new_window = NewBDWindow(self)
        self.new_window.show()
        self.close()

    def editOldBD(self):
        self.new_window = EditOldBDWindow(self)
        self.new_window.show()
        self.close()
