from PySide6.QtWidgets import QApplication

from create_timetable import CreateTimetable

if __name__ == '__main__':
    courses = ["Васильчиков. Программирование в Windows", "Васильев. Как уебать человека кирпичом",
               "Копатыч. Физкультура 2.0", "Лагутина. Изучаем PySide без боли и страха"]
    groups = ["ИВТ-31", "ИВТ-32", "ИТ-31", "ИТ-32", "ПИЭ-31", "ПИЭ-32", "kfgjkdkgdkgk",
              "jgkjdkgjgkn"]
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    number_of_classes_per_day = 4
    app = QApplication([])
    window = CreateTimetable(courses, groups, days, number_of_classes_per_day)
    window.show()
    app.exec()
