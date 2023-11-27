from PySide6.QtWidgets import QApplication

from windows.pre_timetable_windows.start_window import StartWindow

if __name__ == '__main__':
    app = QApplication([])
    window = StartWindow()
    window.showMaximized()
    app.exec()
