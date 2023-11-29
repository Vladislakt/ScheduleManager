from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# Стартовое окно
# from windows.pre_timetable_windows.old_bd_window import EditOldBDWindow
# from windows.pre_timetable_windows.new_bd_window import NewBDWindow


class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройка окна
        self.setMinimumHeight(800)
        self.setMinimumWidth(900)
        self.setWindowTitle("OOO Knopocnie Kabanchiki 3C++")

        # Кнопки в окне
        button_create = QPushButton("Создать")
        button_create.setObjectName("baseButton")
        button_edit = QPushButton("Редактировать")
        button_edit.setObjectName("baseButton")
        button_exit = QPushButton("Выйти")
        button_exit.setObjectName("baseButton")

        # Стиль кнопок
        button_create.setFont(QFont("Georgia", 40))

        button_edit.setFont(QFont("Georgia", 40))

        button_exit.setFont(QFont("Georgia", 40))

        # Размер кнопок
        button_create.setMinimumSize(350, 100)
        button_edit.setMinimumSize(350, 100)
        button_exit.setMinimumSize(200, 100)

        layout = QGridLayout()

        # Устанавливаем кнопки с помощью сетки
        layout.addWidget(button_create, 0, 0, 1, 2)
        layout.addWidget(button_edit, 0, 2, 1, 2)
        layout.addWidget(button_exit, 1, 1, 1, 2)

        # Центруем кнопки
        layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        # При нажатии кнопки выход -> закрывается приложение
        # button_exit.clicked.connect(self.close)
        #
        # При нажатии кнопки создать -> Скрывается это окно -> Переходит на окно создания
        # button_create.clicked.connect(self.createNewBD)
        #
        # button_edit.clicked.connect(self.editOldBD)

    # def createNewBD(self):
    #     self.new_window = NewBDWindow(self)
    #     self.new_window.showMaximized()
    #     self.close()
    #
    # def editOldBD(self):
    #     self.new_window = EditOldBDWindow(self)
    #     self.new_window.showMaximized()
    #     self.close()
