import DataBase.get_list_from_db as h
from DataBase.create_database import create_database
from DataBase.insert_classrooms import insert_classrooms
from DataBase.insert_groups import insert_groups
from DataBase.insert_lessons import insert_lessons
from DataBase.insert_teachers import insert_teachers

current_database = "test"

# create_database(current_database)
#
# teachers = ["Иванов", "Петров", "Сидоров"]
# insert_teachers(current_database, teachers)
#
# groups = [("ИВТ-31бо", 30), ("ИВТ-32бо", 25), ("ИТ-23бо", 12)]
# insert_groups(current_database, groups)
#
# classrooms = [["A102", 40, True, 0], ["B206", 20, True, 21], ["203", 55, False, 1], ["312", 30, False, 0]]
# insert_classrooms(current_database, classrooms)
#
# lessons = [[1, "ИВТ-31бо", 5, "Промышленная разработка", True, False],
#            [2, "ИВТ-32бо", 3, "КСЕ", False, False]]
# insert_lessons(current_database, lessons)

print(h.getLessonsByGroup(current_database, "ИВТ-31бо"))
