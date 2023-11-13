from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from start_window import Start_window

app = QApplication([])
qss_file = QFile("style.qss")
qss_file.open(QFile.ReadOnly | QFile.Text)
stream = QTextStream(qss_file)
app.setStyleSheet(stream.readAll())
window = Start_window()
window.showMaximized()
app.exec()