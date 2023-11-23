import random
from random import randint

from faker import Faker

from DataBase.create_database import create_database
from DataBase.insert_classrooms import insert_classrooms
from DataBase.insert_groups import insert_groups
from DataBase.insert_lessons import insert_lessons
from DataBase.insert_teachers import insert_teachers

fake = Faker('ru_RU')
current_database = "test"

create_database(current_database)

teachers = ["Васильчиков", "Василье", "Бонд"]
for _ in range(20):
    teachers.append(fake.name())
insert_teachers(current_database, teachers)

groups = [("ИВТ-31бо", 30), ("ИВТ-32бо", 25), ("ИТ-23бо", 12)]
for _ in range(20):
    num = fake.random_int(11, 43)
    group = ""
    for _ in range(fake.random_int(1, 3)):
        group += chr(randint(ord('А'), ord('Я')))
    group = f'{group}-{num}бо'
    groups.append((group, fake.random_int(15, 30)))
insert_groups(current_database, groups)

classrooms = [["A102", 40, True, 0], ["B206", 20, True, 21], ["223", 55, False, 1], ["312", 30, False, 0]]
for _ in range(20):
    classroom = fake.random_int(100, 999)
    letter = chr(randint(ord('А'), ord('Я')))
    classroom = f'{letter}{classroom}'
    classrooms.append((classroom, fake.random_int(25, 100), fake.pybool(), fake.random_int(15, 30)))
insert_classrooms(current_database, classrooms)

lessons = [[1, "ИВТ-31бо", 5, "Промышленная разработка", True, False],
           [2, "ИВТ-32бо", 3, "КСЕ", False, False]]
for _ in range(100):
    tech_id = fake.random_int(1, len(teachers))
    group = (random.choice(groups))[0]
    quantity = fake.random_int(1, 3)
    name = ""
    for _ in range(fake.random_int(1, 5)):
        if fake.random_int(0, 1):
            name += chr(randint(ord('А'), ord('Я'))) + " "
        else:
            name += fake.word() + " "
    lessons.append((tech_id, group, quantity, name, fake.pybool(), fake.pybool()))
insert_lessons(current_database, lessons)
