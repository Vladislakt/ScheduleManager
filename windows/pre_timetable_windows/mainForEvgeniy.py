from pathlib import Path

from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from start_window import StartWindow
from add_information_window import AddInformationWindow
from new_bd_window import NewBDWindow
from old_bd_window import OldBDButton, EditOldBDWindow
from add_triple_window import AddTripleWindow
from add_lesson_window import AddLessonWindow
# Расположение окон в проекте:
# main -> pre_timetable_windows -> create_start_window -> addTeacher -> addGroup -> addLeson -> addClassroom

# Если будет не лень сделаю
# # Шрифт
#
# # Путь к файлу шрифта
# font_path = "ofont.ru_Verdana.ttf"
# # Загрузка шрифта
# font_id = QFontDatabase.addApplicationFont(font_path)
# if font_id != 1:
#     # Получение имени шрифта
#     font_name = QFontDatabase.applicationFontFamilies(font_id)[0]
from windows.pre_timetable_windows.add_information_window import AddInformationWindow

app = QApplication(sys.argv)

# Подключение QSS
qss_file = QtCore.QFile(r"style.qss")
qss_file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
stream = QtCore.QTextStream(qss_file)
app.setStyleSheet(stream.readAll())

window = AddInformationWindow(None,'test')
# window = StartWindow()
window.show()
app.exec()
