from PySide6.QtWidgets import QApplication

from create_timetable import CreateTimetable


if __name__ == '__main__':
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    number_of_classes_per_day = 4
    app = QApplication([])
    window = CreateTimetable(days, number_of_classes_per_day)
    window.showMaximized()
    window.show()
    app.exec()
