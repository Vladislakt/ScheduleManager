from PySide6.QtWidgets import QApplication

from windows.pre_timetable_windows.add_lesson_window import AddLessonWindow
from windows.pre_timetable_windows.add_triple_window import AddTripleWindow
from windows.pre_timetable_windows.old_bd_window import EditOldBDWindow

app = QApplication([])
window = EditOldBDWindow(None)
window.showMaximized()
app.exec()
