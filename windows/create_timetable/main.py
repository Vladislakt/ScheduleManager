from PySide6.QtWidgets import QApplication

from timetable_window import TimetableWindow

if __name__ == '__main__':
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    number_of_classes_per_day = 4
    app = QApplication([])
    window = TimetableWindow(days, number_of_classes_per_day)
    window.showMaximized()
    window.show()
    app.exec()
