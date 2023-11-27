from PySide6.QtCore import Qt, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout, QLabel, QScrollArea

from DataBase.get_list_from_db import getTeacherList


# Виджет для добавления преподователей
class AddTeacherWidget(QWidget):
    def __init__(self, current_database):
        super().__init__()
        self.data_masive = []
        title = QWidget()
        self.column_size = [200, 55]
        title_layout = QHBoxLayout()
        title_layout.setAlignment(Qt.AlignLeft)
        t1 = QLabel("Преподователи")
        t1.setFixedWidth(self.column_size[0])
        t2 = QLabel("Удаление")
        t2.setFixedWidth(self.column_size[1])
        title_layout.addWidget(t1)
        title_layout.addWidget(t2)
        title.setLayout(title_layout)
        self.data_masive.append(title)
        main_layout = QVBoxLayout()
        self.plus_button = QPushButton("Добавить строчку")
        self.plus_button.setFixedWidth(120)
        self.plus_button.clicked.connect(self.addLine)
        scroll_area = QScrollArea()
        scroll_area.setFixedSize(320, 480)
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
        self.setFixedSize(350, 530)

        list = getTeacherList(current_database)
        if len(list) > 0:
            for item in list:
                self.getFromItem(item)
            self.updateLayout()
        else:
            self.addLine()

    def getFromItem(self, item):
        line = QWidget()
        teacher = QLineEdit()
        teacher.setText(item.fullname)
        teacher.setFixedWidth(self.column_size[0])
        teacher.setValidator(QRegularExpressionValidator(QRegularExpression("[^0-9]*")))
        cancel_button = QPushButton("X")
        cancel_button.setFixedWidth(self.column_size[1])
        line_layout = QHBoxLayout()
        line_layout.setAlignment(Qt.AlignLeft)
        line_layout.addWidget(teacher)
        line_layout.addWidget(cancel_button)
        line.setLayout(line_layout)
        line.setFixedHeight(40)
        self.data_masive.append(line)
        cancel_button.clicked.connect(lambda: self.delLine(self.data_masive.index(line)))
    def addLine(self):
        line = QWidget()
        teacher = QLineEdit()
        teacher.setFixedWidth(self.column_size[0])
        teacher.setValidator(QRegularExpressionValidator(QRegularExpression("[^0-9]*")))
        cancel_button = QPushButton("X")
        cancel_button.setFixedWidth(self.column_size[1])
        line_layout = QHBoxLayout()
        line_layout.setAlignment(Qt.AlignLeft)
        line_layout.addWidget(teacher)
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
