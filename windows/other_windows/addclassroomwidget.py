from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout, QLabel, QScrollArea, QCheckBox

from DataBase.get_list_from_db import getClassroomList


# Виджет для добавления аудитории
class AddingClassroomWidget(QWidget):
    def __init__(self, current_database):
        super().__init__()
        self.data_masive = []
        title =QWidget()
        self.column_size = [70,74,60,77,55]
        title_layout = QHBoxLayout()
        title_layout.setAlignment(Qt.AlignLeft)
        t1 = QLabel("№ Кабинета")
        t1.setFixedWidth(self.column_size [0])
        t2 = QLabel("Вместимость")
        t2.setFixedWidth(self.column_size[1])
        t3 = QLabel("Проектор")
        t3.setFixedWidth(self.column_size[2])
        t4 = QLabel("Кол-во\nкомпьютеров")
        t4.setFixedWidth(self.column_size[3])
        t5 = QLabel("Удаление")
        t5.setFixedWidth(self.column_size[4])
        title_layout.addWidget(t1)
        title_layout.addWidget(t2)
        title_layout.addWidget(t3)
        title_layout.addWidget(t4)
        title_layout.addWidget(t5)
        title.setLayout(title_layout)
        self.data_masive.append(title)
        main_layout = QVBoxLayout()
        self.plus_button = QPushButton("Добавить строчку")
        self.plus_button.setFixedWidth(120)
        self.plus_button.clicked.connect(self.addLine)
        scroll_area = QScrollArea()
        scroll_area.setFixedSize(416,460)
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
        #self.addLine()
        self.setFixedSize(436, 510)
        list = getClassroomList(current_database)
        if len(list) > 0:
            for item in list:
                self.getFromItem(item)
            self.updateLayout()
        else:
            self.addLine()

    def getFromItem(self, item):
        line = QWidget()
        classroom = QLineEdit()
        classroom.setText(item.class_number)
        classroom.setFixedWidth(self.column_size[0])
        size = QLineEdit()
        size.setText(str(item.max_size))
        size.setFixedWidth(self.column_size[1])
        size.setValidator(QIntValidator())
        projector = QCheckBox()
        projector.setChecked(item.projector)
        projector.setStyleSheet("padding: 22; ")
        projector.setFixedWidth(self.column_size[2])
        computer = QLineEdit()
        computer.setText(str(item.computers))
        computer.setFixedWidth(self.column_size[3])
        computer.setValidator(QIntValidator())
        cancel_button = QPushButton("X")
        cancel_button.setFixedWidth(self.column_size[4])

        line_layout = QHBoxLayout()
        line_layout.setAlignment(Qt.AlignLeft)
        line_layout.addWidget(classroom)
        line_layout.addWidget(size)
        line_layout.addWidget(projector)
        line_layout.addWidget(computer)
        line_layout.addWidget(cancel_button)
        line.setLayout(line_layout)
        line.setFixedHeight(40)
        self.data_masive.append(line)
        cancel_button.clicked.connect(lambda: self.delLine(self.data_masive.index(line)))
    def addLine(self):
        line = QWidget()
        classroom = QLineEdit()
        classroom.setFixedWidth(self.column_size[0])
        size = QLineEdit()
        size.setFixedWidth(self.column_size[1])
        size.setValidator(QIntValidator())
        projector = QCheckBox()
        projector.setStyleSheet("padding: 22; ")
        projector.setFixedWidth(self.column_size[2])
        computer = QLineEdit()
        computer.setFixedWidth(self.column_size[3])
        computer.setValidator(QIntValidator())
        cancel_button = QPushButton("X")
        cancel_button.setFixedWidth(self.column_size[4])

        line_layout = QHBoxLayout()
        line_layout.setAlignment(Qt.AlignLeft)
        line_layout.addWidget(classroom)
        line_layout.addWidget(size)
        line_layout.addWidget(projector)
        line_layout.addWidget(computer)
        line_layout.addWidget(cancel_button)
        line.setLayout(line_layout)
        line.setFixedHeight(40)
        self.data_masive.append(line)
        cancel_button.clicked.connect(lambda: self.delLine(self.data_masive.index(line)))
        self.updateLayout()

    def delLine(self, num_in_list):
        self.data_masive.pop(num_in_list)
        self.updateLayout()

    def clearLayout(self):
        for i in reversed(range(self.scroll_layout.count())):
            self.scroll_layout.itemAt(i).widget().setParent(None)

    def updateLayout(self):
        self.clearLayout()
        for index in range(len(self.data_masive)):
            self.scroll_layout.addWidget(self.data_masive[index])
