import os

from PySide6.QtGui import QFont, Qt, QFontDatabase
from PySide6.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget, QVBoxLayout, QGridLayout, QLabel, \
    QMainWindow

from database.get_list_from_db import getDBName
# from windows.pre_timetable_windows.add_triple_window import AddTripleWindow


def getPathToFinaldata():
    path = "finaldata"
    while True:
        if os.path.isdir(path):
            break
        else:
            path = "../" + path
    rsp_list = []
    for f in os.scandir(path):
        if f.is_file() and f.path.split('.')[-1].lower() == 'rsp':
            rsp_list.append(f.name.split('.')[0])
    return rsp_list


class OldBDButton(QWidget):
    def __init__(self, pre_window, name, filename):
        super().__init__()
        self.pre_window = pre_window
        self.button = QPushButton(name)
        self.button.setObjectName("old_button_namebd")
        self.button.setFont(QFont('Times', 10))
        self.filename = filename
        # self.button.clicked.connect(self.openTripleWindow)
        layout = QHBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    # def openTripleWindow(self):
    #     self.new_window = AddTripleWindow(self.pre_window, self.filename)
    #     self.new_window.showMaximized()
    #     self.pre_window.close()


class EditOldBDWindow(QMainWindow):
    def __init__(self, pre_window):
        super().__init__()

        # Создание объекта предыдущего окна
        self.pre_window = pre_window
        self.setFixedSize(1280, 720)
        self.setWindowTitle("OOO Knopocnie Kabanchiki 3C++")
        self.setFont(QFont("Georgia", 20))

        label = QLabel("Выберите расписание из ранее созданных вами:")

        label.setStyleSheet("color: white")

        id = QFontDatabase.addApplicationFont("Fonts/RobotoSlab.ttf")
        families = QFontDatabase.applicationFontFamilies(id)

        label.setFont(QFont(families, 20))

        label.setAlignment(Qt.AlignCenter)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(label)
        rsp_list = getPathToFinaldata()
        count = 3
        row = 0
        column = 0
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignCenter)
        for i in range(len(rsp_list)):
            button_back = OldBDButton(self, getDBName(rsp_list[i]), rsp_list[i])
            layout.addWidget(button_back, row, i % count)
            column += 1
            if column % count == 0:
                row += 1

        widget = QWidget()
        widget.setLayout(layout)
        button_back = QPushButton("Назад")
        button_back.setObjectName("back_oldbd_long")
        button_back.setFixedSize(670, 25)
        button_back.setFont(QFont('Times', 10))

        # button_back.clicked.connect(self.openPreWindow)

        # scroll_area = QScrollArea()
        # scroll_widget = QWidget()
        # scroll_layout = QHBoxLayout()
        # scroll_layout.addWidget(widget)
        # scroll_widget.setLayout(scroll_layout)
        # scroll_area.setWidget(scroll_widget)

        main_layout.addWidget(widget)
        # main_layout.addWidget(scroll_area)
        main_layout.addWidget(button_back)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

    # def openPreWindow(self):
    #     self.pre_window.showMaximized()
    #     self.destroy()
