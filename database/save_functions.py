from database.create_session import create_session
from models.cell import Cell
from models.classrooms import Classrooms
from models.groups import Groups
from models.lessons import Lessons
from models.teachers import Teachers


def save_teachers(filename, teacher_list, id_list):
    session = create_session(filename)
    list = session.query(Teachers).all()
    # Удаление из бд тех записей, которые были убраны на виджете
    for item in list:
        if item.teach_id not in id_list:
            session.delete(item)
    # Вставка/обновление в бд тех записей, которые есть на виджете
    for index in range(1, len(teacher_list)):
        id = id_list[index - 1]
        name = teacher_list[index].teacher.text()
        teacher = session.query(Teachers).filter(Teachers.teach_id == id).first()
        if teacher is None:
            teacher = Teachers(teach_id=id)
        teacher.fullname = name
        session.add(teacher)
    session.commit()
    session.close()


def save_groups(filename, group_list):
    name_list = []
    for index in range(1, len(group_list)):
        name_list.append(group_list[index].group.text())
    session = create_session(filename)
    list = session.query(Groups).all()
    # Удаление из бд тех записей, которые были убраны на виджете
    for item in list:
        if item.group_name not in name_list:
            session.delete(item)
    # Вставка/обновление в бд тех записей, которые есть на виджете
    for index in range(1, len(group_list)):
        group_name = name_list[index - 1]
        size = int(group_list[index].size.text())
        group = session.query(Groups).filter(Groups.group_name == group_name).first()
        if group is None:
            group = Groups(group_name=group_name)
        group.size = size
        session.add(group)
    session.commit()
    session.close()


def save_classrooms(filename, classroom_list):
    name_list = []
    for index in range(1, len(classroom_list)):
        name_list.append(classroom_list[index].classroom.text())
    session = create_session(filename)
    list = session.query(Classrooms).all()
    # Удаление из бд тех записей, которые были убраны на виджете
    for item in list:
        if item.class_number not in name_list:
            session.delete(item)
    # Вставка/обновление в бд тех записей, которые есть на виджете
    for index in range(1, len(classroom_list)):
        class_number = name_list[index - 1]
        max_size = int(classroom_list[index].size.text())
        projector = classroom_list[index].projector.isChecked()
        computer = int(classroom_list[index].computer.text())
        classroom = session.query(Classrooms).filter(Classrooms.class_number == class_number).first()
        if classroom is None:
            classroom = Classrooms(class_number=class_number)
        classroom.max_size = max_size
        classroom.projector = projector
        classroom.computers = computer
        session.add(classroom)
    session.commit()
    session.close()


def save_lessons(filename, lesson_list, id_list):
    session = create_session(filename)
    list = session.query(Lessons).all()
    # Удаление из бд тех записей, которые были убраны на виджете
    for item in list:
        if item.id not in id_list:
            session.delete(item)
    # Вставка/обновление в бд тех записей, которые есть на виджете
    for index in range(1, len(lesson_list)):
        id = id_list[index - 1]
        teach_id = lesson_list[index].teacher.currentIndex()
        group_name = lesson_list[index].group.currentText()
        lesson_name = lesson_list[index].lesson.text()
        quantity = int(lesson_list[index].quantity.text())
        projector = lesson_list[index].projector.isChecked()
        computer = lesson_list[index].computer.isChecked()
        lesson = session.query(Lessons).filter(Lessons.id == id).first()
        if lesson is None:
            lesson = Lessons(id=id)
        lesson.teach_id = teach_id
        lesson.group_name = group_name
        lesson.lesson_name = lesson_name
        lesson.quantity = quantity
        lesson.projector = projector
        lesson.computers = computer
        session.add(lesson)
    session.commit()
    session.close()


def save_finaldata(filename, cell_list):
    session = create_session(filename)
    list = session.query(Cell).all()
    # Удаление из бд тех записей, которые были убраны
    for item in list:
        if item not in cell_list:
            session.delete(item)
    # Вставка/обновление в бд тех записей, которые есть
    for cell in cell_list:
        day = cell.day
        group = cell.group
        number_of_class = cell.number_of_class
        lesson_id = cell.lesson_id
        classroom = cell.classroom
        new_cell = session.query(Cell).filter(Cell.day == day,
                                              Cell.group == group,
                                              Cell.number_of_class == number_of_class
                                              ).first()
        if new_cell is None:
            new_cell = Cell(group, day, number_of_class, lesson_id, classroom)
        else:
            new_cell.lesson_id = lesson_id
            new_cell.classroom = classroom
        session.add(new_cell)
    session.commit()
    session.close()
