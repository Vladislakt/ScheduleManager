from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from start_window import Start_window

app = QApplication([])
app.setStyleSheet(Path('style.qss').read_text())
window = Start_window()
window.showMaximized()
app.exec()