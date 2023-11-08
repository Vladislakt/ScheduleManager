from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea

from buttons import Buttons


class Courses(QWidget):
    def __init__(self, courses):
        super().__init__()
        # self.setStyleSheet("background-color: rgb(255,255,255); ")
        self.courses = courses
        self.layout = QVBoxLayout()
        self.add_header()
        self.add_courses()
        self.add_buttons()
        self.setLayout(self.layout)

    def add_header(self):
        label = QLabel("Список курсов")
        self.layout.addWidget(label)

    def add_courses(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        for i in range(len(self.courses)):
            course = QLabel(self.courses[i])
            layout.addWidget(course)
        widget = QWidget()
        widget.setLayout(layout)
        scroll_area.setWidget(widget)
        self.layout.addWidget(scroll_area)

    def add_buttons(self):
        buttons = Buttons()
        self.layout.addWidget(buttons)
