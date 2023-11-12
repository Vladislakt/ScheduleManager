from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QWidget, QHBoxLayout, QApplication, QPushButton, QTextEdit, QLineEdit, QLabel, \
    QVBoxLayout, QGridLayout, QLayoutItem, QScrollBar, QScrollArea, QLayout


class LineMassive(QWidget):
    def __init__(self):
        super().__init__()
        self.massive = []
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)
        self.addLine()

    def addLine(self):
        line = QWidget()
        line.setFixedSize(500, 40)
        line.button = QPushButton("+")
        line.line = QLineEdit()
        line.cancel_button = QPushButton("X")

        line.button.clicked.connect(self.addLine)
        line.cancel_button.clicked.connect(lambda: self.delLine(self.massive.index(line)))

        line_layout = QGridLayout()
        line_layout.addWidget(line.button, 0, 0)
        line_layout.addWidget(line.line, 0, 1)
        line_layout.addWidget(line.cancel_button, 0, 2)
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

        scroll_area = QScrollArea()
        scroll_area.setWidget(m)
        scroll_area.setWidgetResizable(True)

        mainLayout.addWidget(scroll_area)

        self.setLayout(mainLayout)


app = QApplication([])
window = TestWindow()
window.show()
app.exec()
