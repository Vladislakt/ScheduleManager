from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout, QComboBox, QCheckBox, QLabel, QScrollArea


# Виджет для добавления предметов

class AddLessonWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.data_masive = []
        title = QWidget()
        self.column_size = [200, 70, 70, 70, 60, 75, 55]
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
        scroll_area.setFixedSize(695, 460)
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
        self.addLine()
        self.setFixedSize(705, 510)

    def addLine(self):
        line = QWidget()
        teacher = QComboBox()
        teacher.setFixedWidth(self.column_size[0])
        group = QComboBox()
        group.setFixedWidth(self.column_size[1])
        lesson = QLineEdit()
        lesson.setFixedWidth(self.column_size[2])
        quantity = QLineEdit()
        quantity.setFixedWidth(self.column_size[3])
        quantity.setValidator(QIntValidator())
        projector = QCheckBox()
        projector.setStyleSheet("padding: 22; ")
        projector.setFixedWidth(self.column_size[4])
        computer = QCheckBox()
        computer.setStyleSheet("padding: 22; ")
        computer.setFixedWidth(self.column_size[5])
        cancel_button = QPushButton("X")
        cancel_button.setFixedWidth(self.column_size[6])

        line_layout = QHBoxLayout()
        line_layout.setAlignment(Qt.AlignLeft)
        line_layout.addWidget(teacher)
        line_layout.addWidget(group)
        line_layout.addWidget(lesson)
        line_layout.addWidget(quantity)
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
