from database.create_database import create_database
from database.insert_classrooms import insert_classrooms
from database.insert_groups import insert_groups
from database.insert_information import insert_information
from database.insert_lessons import insert_lessons
from database.insert_name import insert_name
from database.insert_teachers import insert_teachers

# current_database = "test"

current_database = create_database()

insert_name(current_database, "Тестовая")

insert_information(current_database, True, 5)

teachers = ["Васильчиков В", "Васильев А", "Сажин С", "Бондаренко В", "Николаев А", "Шовгенов Д", "Мусин М",
            "Волчёнков В",
            "Ларина Ю", "Ануфриенко М", "Смирнов Я", "Данилов Д", "Лагутина К", "Лавровская И", "Морозов Е",
            "Мастакова И",
            "Седов М", "Чалый Д", "Парамонов К", "Полеаев А", "Федулов Д", "Кузьмин Е", "Богомолов А", "Чвягина Е",
            "Капатыч А",
            "Белов ", "Шабаршина", "Смирнов.А", "Адрианова", "Чистяков"]
insert_teachers(current_database, teachers)

groups = [("ИВТ-11БО", 25), ("ИВТ-12БО", 25), ("ИВТ-13БО", 25), ("ИТ-11БО", 20), ("ИТ-12БО", 20), ("ПИЭ-11БО", 15),
          ("ПИЭ-12БО", 15),
          ("ИВТ-21БО", 23), ("ИВТ-22БО", 24), ("ИВТ-23БО", 21), ("ИТ-21БО", 18), ("ИТ-22БО", 16), ("ПИЭ-21БО", 12),
          ("ПИЭ-22БО", 13),
          ("ИВТ-31БО", 30), ("ИВТ-32БО", 32), ("ИТ-31БО", 20), ("ИТ-32БО", 18), ("ПИЭ-31БО", 12), ("ПИЭ-32БО", 12),
          ("ИВТ-41БО", 28), ("ИВТ-42БО", 29), ("ИТ-41БО", 35), ("ПИЭ-41БО", 11), ("ПИЭ-42БО", 10),
          ("ИВТ-13МО", 7), ("ИТ-12МО", 5), ("ПИЭ-13МО", 5),
          ("ИВТ-23МО", 6), ("ИТ-22МО", 4), ("ПИЭ-23МО", 4), ]
insert_groups(current_database, groups)

classrooms = [["201", 20, False, 0], ["203", 30, False, 0], ["207", 30, True, 1], ["209", 30, True, 30],
              ["210", 35, True, 35], ["211", 20, True, 20], ["212", 30, False, 0], ["215", 100, True, 1],
              ["216", 50, True, 35], ["219", 35, False, 0], ["220", 120, True, 1], ["224", 30, True, 16],
              ["225", 50, True, 1],
              ["301", 75, True, 1], ["306", 25, True, 1], ["310", 50, True, 1], ["312", 80, True, 0],
              ["402", 40, True, 30], ["406", 30, True, 30], ["412", 30, True, 1], ["415", 100, True, 1],
              ["418", 25, True, 1], ["419", 120, True, 1]]
insert_classrooms(current_database, classrooms)

lessons = [
    [5, "ИВТ-11БО", 4, "Алгебра и геометрия", True, True],
    [7, "ИВТ-11БО", 1, "Основы Российской государственности", False, False],
    [8, "ИВТ-11БО", 1, "Основы информатики", False, False],
    [11, "ИВТ-11БО", 1, "Основы Российской государственности", True, False],
    [9, "ИВТ-11БО", 1, "Практикум на ЭВМ по основам программирования", True, False],
    [24, "ИВТ-11БО", 1, "Иностранный язык", False, False],
    [10, "ИВТ-11БО", 2, "Практикум по математическому анализу", False, False],
    [25, "ИВТ-11БО", 2, "Прикладная физическая культура", False, False],
    [1, "ИВТ-11БО", 2, "Основы програмирования", True, False],
    [4, "ИВТ-11БО", 2, "Математический анализ", True, False],
    [13, "ИВТ-11БО", 1, "Основы информатики", True, True],
    [3, "ИВТ-11БО", 1, "Дискретная математика и математическая логика", True, False],
    [26, "ИВТ-11БО", 1, "Дискретная математика и математическая логика", True, False],
    [12, "ИВТ-11БО", 1, "История России с древнейших времен до конца XVIII века", True, False],
    [5, "ИВТ-12БО", 4, "Алгебра и геометрия", True, True],
    [7, "ИВТ-12БО", 1, "Основы Российской государственности", False, False],
    [8, "ИВТ-12БО", 1, "Основы информатики", False, False],
    [11, "ИВТ-12БО", 1, "Основы Российской государственности", True, False],
    [9, "ИВТ-12БО", 1, "Практикум на ЭВМ по основам программирования", True, False],
    [24, "ИВТ-12БО", 1, "Иностранный язык", False, False],
    [10, "ИВТ-12БО", 2, "Практикум по математическому анализу", False, False],
    [25, "ИВТ-12БО", 2, "Прикладная физическая культура", False, False],
    [1, "ИВТ-12БО", 2, "Основы програмирования", True, False],
    [4, "ИВТ-12БО", 2, "Математический анализ", True, False],
    [13, "ИВТ-12БО", 1, "Основы информатики", True, True],
    [3, "ИВТ-12БО", 1, "Дискретная математика и математическая логика", True, False],
    [26, "ИВТ-12БО", 1, "Дискретная математика и математическая логика", True, False],
    [12, "ИВТ-12БО", 1, "История России с древнейших времен до конца XVIII века", True, False],
    [5, "ИВТ-13БО", 4, "Алгебра и геометрия", True, True],
    [7, "ИВТ-13БО", 1, "Основы Российской государственности", False, False],
    [8, "ИВТ-13БО", 1, "Основы информатики", False, False],
    [11, "ИВТ-13БО", 1, "Основы Российской государственности", True, False],
    [9, "ИВТ-13БО", 1, "Практикум на ЭВМ по основам программирования", True, False],
    [24, "ИВТ-13БО", 1, "Иностранный язык", False, False],
    [10, "ИВТ-13БО", 2, "Практикум по математическому анализу", False, False],
    [25, "ИВТ-13БО", 2, "Прикладная физическая культура", False, False],
    [1, "ИВТ-13БО", 2, "Основы програмирования", True, False],
    [4, "ИВТ-13БО", 2, "Математический анализ", True, False],
    [13, "ИВТ-13БО", 1, "Основы информатики", True, True],
    [3, "ИВТ-13БО", 1, "Дискретная математика и математическая логика", True, False],
    [26, "ИВТ-13БО", 1, "Дискретная математика и математическая логика", True, False],
    [12, "ИВТ-13БО", 1, "История России с древнейших времен до конца XVIII века", True, False],
    [11, "ИТ-11БО", 1, "Основы Российской государственности", True, False],
    [10, "ИТ-11БО", 2, "Математический анализ", False, False],
    [27, "ИТ-11БО", 2, "Математический анализ", False, False],
    [8, "ИТ-11БО", 1, "Основы информатики", False, False],
    [28, "ИТ-11БО", 2, "Дискретная математика", False, False],
    [16, "ИТ-11БО", 1, "Иностранный язык", False, False],
    [7, "ИТ-11БО", 1, "Основы Российской государственности", False, False],
    [1, "ИТ-11БО", 2, "Основы програмирования", True, False],
    [29, "ИТ-11БО", 1, "Практикум на ЭВМ по информатике", True, True],
    [25, "ИТ-11БО", 2, "Прикладная физическая культура", False, False],
    [9, "ИТ-11БО", 1, "Практикум на ЭВМ по основам программирования", True, False],
    [11, "ИТ-12БО", 1, "Основы Российской государственности", True, False],
    [10, "ИТ-12БО", 2, "Математический анализ", False, False],
    [27, "ИТ-12БО", 2, "Математический анализ", False, False],
    [8, "ИТ-12БО", 1, "Основы информатики", False, False],
    [28, "ИТ-12БО", 2, "Дискретная математика", False, False],
    [16, "ИТ-12БО", 1, "Иностранный язык", False, False],
    [7, "ИТ-12БО", 1, "Основы Российской государственности", False, False],
    [1, "ИТ-12БО", 2, "Основы програмирования", True, False],
    [29, "ИТ-12БО", 1, "Практикум на ЭВМ по информатике", True, True],
    [25, "ИТ-12БО", 2, "Прикладная физическая культура", False, False],
    [9, "ИТ-12БО", 1, "Практикум на ЭВМ по основам программирования", True, False],
    [14, "ПИЭ-11БО", 2, "Алгоритмизация и программирование", True, True],
    [15, "ПИЭ-11БО", 2, "Математика", True, False],
    [11, "ПИЭ-11БО", 1, "Основы Российской государственности", True, False],
    [16, "ПИЭ-11БО", 1, "Иностранный язык", False, False],
    [25, "ИТ-12БО", 2, "Прикладная физическая культура", False, False],
    [30, "ПИЭ-11БО", 1, "Экономическая теория", True, False],
    [7, "ИВТ-11БО", 1, "Основы Российской государственности", False, False],
    [13, "ПИЭ-11БО", 1, "Алгоритмизация и программирование", True, True],
    [15, "ПИЭ-11БО", 1, "Математические основы вычислительной техники", True, False],
    [14, "ПИЭ-11БО", 2, "Алгоритмизация и программирование", True, True],
    [15, "ПИЭ-11БО", 2, "Математика", True, False],
    [11, "ПИЭ-11БО", 1, "Основы Российской государственности", True, False],
    [16, "ПИЭ-11БО", 1, "Иностранный язык", False, False],
    [25, "ПИЭ-12БО", 2, "Прикладная физическая культура", False, False],
    [30, "ПИЭ-11БО", 1, "Экономическая теория", True, False],
    [7, "ПИЭ-11БО", 1, "Основы Российской государственности", False, False],
    [13, "ПИЭ-11БО", 1, "Алгоритмизация и программирование", True, True],
    [15, "ПИЭ-11БО", 1, "Математические основы вычислительной техники", True, False],
    [14, "ПИЭ-12БО", 2, "Алгоритмизация и программирование", True, True],
    [15, "ПИЭ-12БО", 2, "Математика", True, False],
    [11, "ПИЭ-12БО", 1, "Основы Российской государственности", True, False],
    [16, "ПИЭ-12БО", 1, "Иностранный язык", False, False],
    [25, "ПИЭ-12БО", 2, "Прикладная физическая культура", False, False],
    [30, "ПИЭ-12БО", 1, "Экономическая теория", True, False],
    [7, "ПИЭ-12БО", 1, "Основы Российской государственности", False, False],
    [13, "ПИЭ-12БО", 1, "Алгоритмизация и программирование", True, True],
    [15, "ПИЭ-12БО", 1, "Математические основы вычислительной техники", True, False]
]
insert_lessons(current_database, lessons)
