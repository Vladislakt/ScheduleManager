import random

from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout, QComboBox, QCheckBox, QLabel, \
    QScrollArea


# Виджет для добавления предметов
from database.get_list_from_db import getTeacherList, getGroupNameList, getLessonList


class AddLessonWidget(QWidget):
    def __init__(self, current_database):
        super().__init__()
        self.teacher_list = getTeacherList(current_database)
        self.group_list = getGroupNameList(current_database)
        self.data_masive = []
        self.id_massive = []
        title = QWidget()
        self.column_size = [170, 100, 370, 70, 60, 75, 55]
        title_layout = QHBoxLayout()
        title_layout.setAlignment(Qt.AlignLeft)
        t1 = QLabel("Преподователь")
        t1.setFixedWidth(self.column_size[0])
        t2 = QLabel("Группа")
        t2.setFixedWidth(self.column_size[1])
        t3 = QLabel("Предмет")
        t3.setFixedWidth(self.column_size[2])
        t4 = QLabel("Кол-во в\nнеделю")
        t4.setFixedWidth(self.column_size[3])
        t5 = QLabel("Проектор")
        t5.setFixedWidth(self.column_size[4])
        t6 = QLabel("Компьютеры")
        t6.setFixedWidth(self.column_size[5])
        t7 = QLabel("Удаление")
        t7.setFixedWidth(self.column_size[6])
        title_layout.addWidget(t1)
        title_layout.addWidget(t2)
        title_layout.addWidget(t3)
        title_layout.addWidget(t4)
        title_layout.addWidget(t5)
        title_layout.addWidget(t6)
        title_layout.addWidget(t7)
        title.setLayout(title_layout)
        self.data_masive.append(title)
        main_layout = QVBoxLayout()
        self.plus_button = QPushButton("Добавить строчку")
        self.plus_button.setFixedWidth(120)
        self.plus_button.clicked.connect(self.addLine)
        scroll_area = QScrollArea()
        scroll_area.setFixedSize(995, 460)
        self.scroll_vidget = QWidget()
        scroll_area.setWidget(self.scroll_vidget)
        scroll_area.setWidgetResizable(True)
        self.scroll_layout = QVBoxLayout()
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_layout.setSpacing(0)
        self.scroll_vidget.setLayout(self.scroll_layout)
        main_layout.addWidget(scroll_area)
        main_layout.addWidget(self.plus_button)
        self.setLayout(main_layout)
        # self.addLine()
        self.setFixedSize(1005, 510)
        list = getLessonList(current_database)
        if len(list) > 0:
            for item in list:
                self.getFromItem(item)
            self.updateLayout()
        else:
            self.addLine()

    def getFromItem(self, item):
        line = QWidget()
        line.teacher = QComboBox()
        line.teacher.setFixedWidth(self.column_size[0])
        line.teacher.insertItem(0, "<выберите>")
        for element in self.teacher_list:
            line.teacher.insertItem(element.teach_id + 1, element.fullname)
        line.teacher.setCurrentIndex(item.teach_id)
        line.group = QComboBox()
        line.group.setFixedWidth(self.column_size[1])
        line.group.addItem("<выберите>")
        for element in self.group_list:
            line.group.addItem(element)
        line.group.setCurrentText(item.group_name)
        line.lesson = QLineEdit()
        line.lesson.setFixedWidth(self.column_size[2])
        line.lesson.setText(item.lesson_name)
        line.quantity = QLineEdit()
        line.quantity.setFixedWidth(self.column_size[3])
        line.quantity.setValidator(QIntValidator())
        line.quantity.setText(str(item.quantity))
        line.projector = QCheckBox()
        line.projector.setStyleSheet("padding: 22; ")
        line.projector.setFixedWidth(self.column_size[4])
        line.projector.setChecked(item.projector)
        line.computer = QCheckBox()
        line.computer.setStyleSheet("padding: 22; ")
        line.computer.setFixedWidth(self.column_size[5])
        line.computer.setChecked(item.computers)
        cancel_button = QPushButton("X")
        cancel_button.setFixedWidth(self.column_size[6])
        line_layout = QHBoxLayout()
        line_layout.setAlignment(Qt.AlignLeft)
        line_layout.addWidget(line.teacher)
        line_layout.addWidget(line.group)
        line_layout.addWidget(line.lesson)
        line_layout.addWidget(line.quantity)
        line_layout.addWidget(line.projector)
        line_layout.addWidget(line.computer)
        line_layout.addWidget(cancel_button)
        line.setLayout(line_layout)
        line.setFixedHeight(40)
        self.data_masive.append(line)
        id = item.id
        self.id_massive.append(id)
        cancel_button.clicked.connect(lambda: self.delLine(self.data_masive.index(line), id))

    def addLine(self):
        line = QWidget()
        line.teacher = QComboBox()
        line.teacher.setFixedWidth(self.column_size[0])
        line.teacher.insertItem(0, "<выберите>")
        for item in self.teacher_list:
            line.teacher.insertItem(item.teach_id + 1, item.fullname)
        line.group = QComboBox()
        line.group.setFixedWidth(self.column_size[1])
        line.group.addItem("<выберите>")
        for item in self.group_list:
            line.group.addItem(item)
        line.lesson = QLineEdit()
        line.lesson.setFixedWidth(self.column_size[2])
        line.quantity = QLineEdit()
        line.quantity.setFixedWidth(self.column_size[3])
        line.quantity.setValidator(QIntValidator())
        line.projector = QCheckBox()
        line.projector.setStyleSheet("padding: 22; ")
        line.projector.setFixedWidth(self.column_size[4])
        line.computer = QCheckBox()
        line.computer.setStyleSheet("padding: 22; ")
        line.computer.setFixedWidth(self.column_size[5])
        cancel_button = QPushButton("X")
        cancel_button.setFixedWidth(self.column_size[6])

        line_layout = QHBoxLayout()
        line_layout.setAlignment(Qt.AlignLeft)
        line_layout.addWidget(line.teacher)
        line_layout.addWidget(line.group)
        line_layout.addWidget(line.lesson)
        line_layout.addWidget(line.quantity)
        line_layout.addWidget(line.projector)
        line_layout.addWidget(line.computer)
        line_layout.addWidget(cancel_button)
        line.setLayout(line_layout)
        line.setFixedHeight(40)
        self.data_masive.append(line)
        while True:
            id = random.randint(1, 1000)
            if id not in self.id_massive:
                self.id_massive.append(id)
                break
        cancel_button.clicked.connect(lambda: self.delLine(self.data_masive.index(line), id))
        self.updateLayout()

    def delLine(self, num_in_list, id):
        self.data_masive.pop(num_in_list)
        self.id_massive.remove(id)
        self.updateLayout()

    def clearLayout(self):
        for i in reversed(range(self.scroll_layout.count())):
            self.scroll_layout.itemAt(i).widget().setParent(None)

    def updateLayout(self):
        self.clearLayout()
        for index in range(len(self.data_masive)):
            self.scroll_layout.addWidget(self.data_masive[index])
