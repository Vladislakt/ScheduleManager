from PySide6 import QtCore
from PySide6.QtWidgets import QApplication

from windows.pre_timetable_windows.start_window import StartWindow

if __name__ == '__main__':
    app = QApplication([])

    # Подключение QSS
    qss_file = QtCore.QFile(r"style.qss")
    qss_file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(qss_file)
    app.setStyleSheet(stream.readAll())

    window = StartWindow()
    window.show()
    app.exec()
