import os

from PySide6.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget

from DataBase.get_list_from_db import getDBName
from windows.start_window.addTeacher import AddTeacher


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

class Button(QWidget):
    def __init__(self, editingwindow, name, filename):
        super().__init__()
        self.editingwindow = editingwindow
        self.button = QPushButton(name)
        self.filename = filename
        self.button.clicked.connect(self.openNextWindow)
        layout = QHBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)
    def openNextWindow(self):
        self.switch_window = AddTeacher(self)
        self.switch_window.showMaximized()
        self.editingwindow.destroy()
class EditingWindow(QWidget):
    def __init__(self):
        super().__init__()
        rsp_list = getPathToFinaldata()
        layout = QHBoxLayout()
        buttons = []
        for i in range(len(rsp_list)):
            button = Button(self, getDBName(rsp_list[i]), rsp_list[i])
            layout.addWidget(button)
        # for i in range(len(buttons)):
        #     layout.addWidget(buttons[i][0])
        self.setLayout(layout)



app = QApplication([])
window = EditingWindow()
window.show()
app.exec()
