from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from start_window import StartWindow

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

app = QApplication([])

# Подключение QSS
qss_file = QFile("style.qss")
qss_file.open(QFile.ReadOnly | QFile.Text)
stream = QTextStream(qss_file)
app.setStyleSheet(stream.readAll())

window = AddInformationWindow(None, "test")
window.showMaximized()
app.exec()
