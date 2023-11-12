from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QWidget, QHBoxLayout, QApplication, QPushButton, QTextEdit, QLineEdit, QLabel, \
    QVBoxLayout, QGridLayout, QLayoutItem, QScrollBar, QScrollArea, QLayout


class LineMassive(QWidget):
    def __init__(self):
        super().__init__()
        self.massive = []
        self.layout = QVBoxLayout()

        self.addLine()
        self.setFixedSize(1000, 600)

    def addLine(self):
        line = QWidget()
        line.setFixedSize(500, 40)
        line.button = QPushButton("+")
        line.line = QLineEdit()
        line.cancel_button = QPushButton("X")

        line.button.clicked.connect(self.addLine)
        line.cancel_button.clicked.connect(lambda: self.delLine(self.massive.index(line)))

        layout = QGridLayout()
        layout.addWidget(line.button, 0, 0)
        layout.addWidget(line.line, 0, 1)
        layout.addWidget(line.cancel_button, 0, 2)
        line.setLayout(layout)

        self.massive.append(line)
        self.updateLayout()

    def delLine(self, num_in_list):
        self.massive.pop(num_in_list)
        self.updateLayout()

    def clearLayout(self):
        for i in reversed(range(self.layout.count())):
            if self.layout.itemAt(i).widget() is None:
                self.layout.removeItem(self.layout.itemAt(i))
            else:
                self.layout.itemAt(i).widget().setParent(None)

    def updateLayout(self):
        self.clearLayout()
        if len(self.massive) == 1:
            self.massive[0].cancel_button.setVisible(False)
            self.massive[0].button.setVisible(True)
            self.layout.addWidget(self.massive[0])
        else:
            for index in range(len(self.massive)):
                if index < len(self.massive) - 1:
                    self.massive[index].button.setVisible(False)
                else:
                    self.massive[index].button.setVisible(True)
                self.massive[index].cancel_button.setVisible(True)
                self.layout.addWidget(self.massive[index])
        self.layout.addStretch()
        self.setLayout(self.layout)


class TestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 700)
        self.setMaximumSize(1200, 700)
        self.setWindowTitle("Тестовый вариант вставки данных")

        title = QLabel("Заголовок")

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(title)

        m = LineMassive()



        mainLayout.addWidget(m)

        # mainLayout.addWidget(m)

        self.setLayout(mainLayout)


app = QApplication([])
window = TestWindow()
window.show()
app.exec()
