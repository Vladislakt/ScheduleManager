import xlsxwriter
from PySide6.QtCore import QDir
from PySide6.QtWidgets import QFileDialog


def fill_xlsx(table, days, number_of_classes_per_day):
    filename = QFileDialog.getSaveFileName(table, "Сохранить в...", str(QDir.currentPath()), "Microsoft Excel 2007 "
                                                                                             "files (*.xlsx)")
    if filename[0] != '':
        workbook = xlsxwriter.Workbook(filename[0])
        worksheet = workbook.add_worksheet()
        insert_days_and_class_numbers(worksheet, days, number_of_classes_per_day)
        insert_groups(worksheet, table)
        insert_courses_and_classrooms(worksheet, table, days, number_of_classes_per_day)
        workbook.close()
        table.were_changes = False


def insert_days_and_class_numbers(worksheet, days, number_of_classes_per_day):
    for i in range(len(days)):
        worksheet.write(i * number_of_classes_per_day + 1, 0, days[i])
        for j in range(number_of_classes_per_day):
            worksheet.write(i * number_of_classes_per_day + j + 1, 1, j + 1)


def insert_groups(worksheet, table):
    for i in range(len(table.group_names)):
        worksheet.write(0, i * 2 + 2, table.group_names[i])


def insert_courses_and_classrooms(worksheet, table, days, number_of_classes_per_day):
    for i in range(len(table.group_names)):
        for j in range(len(days)):
            for k in range(number_of_classes_per_day):
                worksheet.write(j * number_of_classes_per_day + k + 1, i * 2 + 2,
                                table.scroll_area_layout.itemAtPosition(
                                    j * (number_of_classes_per_day + 1) + k + 2,
                                    3 + i * 3).widget().currentText())
                worksheet.write(j * number_of_classes_per_day + k + 1, i * 2 + 3,
                                table.scroll_area_layout.itemAtPosition(
                                    j * (number_of_classes_per_day + 1) + k + 2,
                                    4 + i * 3).widget().currentText())
