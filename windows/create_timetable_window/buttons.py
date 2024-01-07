from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QMessageBox

from windows.create_timetable_window.operations_with_database import write_table_data_to_db
from windows.create_timetable_window.write_xlsx import fill_xlsx


class Buttons(QWidget):
    def __init__(self, db, table, days, number_of_classes_per_day, pre_window, this_window):
        super().__init__()
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignRight)
        save = QPushButton("Сохранить")
        save.clicked.connect(lambda: write_table_data_to_db(db, table, days, number_of_classes_per_day))
        save.clicked.connect(lambda: fill_xlsx(table, days, number_of_classes_per_day))
        to_start = QPushButton("На главную")
        to_start.clicked.connect(lambda: open_start_window(db, table, days, number_of_classes_per_day, pre_window,
                                                           this_window))
        exit = QPushButton("Выход")
        exit.clicked.connect(lambda: leave_app(this_window, db, table, days, number_of_classes_per_day))
        layout.addWidget(save)
        layout.addWidget(to_start)
        layout.addWidget(exit)
        self.setLayout(layout)


def leave_app(this_window, db, table, days, number_of_classes_per_day):
    if table.were_changes:
        warning = QMessageBox()
        warning.setText("Сохранить изменения в файл?")
        warning.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        warning.setDefaultButton(QMessageBox.Save)
        ret = warning.exec()
        if ret == QMessageBox.Save:
            write_table_data_to_db(db, table, days, number_of_classes_per_day)
            fill_xlsx(table, days, number_of_classes_per_day)
            this_window.close()
        elif ret == QMessageBox.Discard:
            write_table_data_to_db(db, table, days, number_of_classes_per_day)
            this_window.close()
    else:
        this_window.close()


def open_start_window(db, table, days, number_of_classes_per_day, pre_window, this_window):
    write_table_data_to_db(db, table, days, number_of_classes_per_day)
    pre_window.pre_window.pre_window.pre_window.pre_window.showMaximized()
    pre_window.pre_window.pre_window.pre_window.destroy()
    pre_window.pre_window.pre_window.destroy()
    pre_window.pre_window.destroy()
    pre_window.destroy()
    this_window.destroy()
