from PySide6.QtCore import QFile, QTextStream
from PySide6.QtWidgets import QApplication

from windows.pre_timetable_windows.add_triple_window import AddTripleWindow

app = QApplication([])
window = AddTripleWindow(None, "test")
window.showMaximized()
app.exec()
