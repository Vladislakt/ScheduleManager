from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from start_window import StartWindow

# Расположение окон в проекте:
# main -> start_window -> create_start_window -> addTeacher -> addGroup -> addLeson -> addClassroom

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

app = QApplication([])

# Подключение QSS
qss_file = QFile("style.qss")
qss_file.open(QFile.ReadOnly | QFile.Text)
stream = QTextStream(qss_file)
app.setStyleSheet(stream.readAll())

window = StartWindow()
window.showMaximized()
app.exec()
