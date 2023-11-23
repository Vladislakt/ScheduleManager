from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout


class AddingTeacherWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.massive = []
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)
        self.addLine()

    def addLine(self):
        line = QWidget()
        line.plus_button = QPushButton("+")
        line.name = QLineEdit()
        line.cancel_button = QPushButton("X")

        line.plus_button.clicked.connect(self.addLine)
        line.cancel_button.clicked.connect(lambda: self.delLine(self.massive.index(line)))

        line_layout = QHBoxLayout()
        line_layout.addWidget(line.plus_button)
        line_layout.addWidget(line.name)
        line_layout.addWidget(line.cancel_button)
        line.setLayout(line_layout)

        self.massive.append(line)
        self.updateLayout()

    def delLine(self, num_in_list):
        self.massive.pop(num_in_list)
        self.updateLayout()

    def clearLayout(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

    def updateLayout(self):
        self.clearLayout()
        if len(self.massive) == 1:
            self.massive[0].cancel_button.setVisible(False)
            self.massive[0].plus_button.setVisible(True)
            self.layout.addWidget(self.massive[0])
        else:
            for index in range(len(self.massive)):
                if index < len(self.massive) - 1:
                    self.massive[index].plus_button.setVisible(False)
                else:
                    self.massive[index].plus_button.setVisible(True)
                self.massive[index].cancel_button.setVisible(True)
                self.layout.addWidget(self.massive[index])