from PySide6.QtWidgets import QApplication

from windows.pre_timetable_windows.add_lesson_window import AddLessonWindow
from windows.pre_timetable_windows.add_triple_window import AddTripleWindow

app = QApplication([])
window = AddLessonWindow(None, "test2")
window.showMaximized()
app.exec()
