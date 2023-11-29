from database.create_session import create_session
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
        # if session.query(Teachers).filter(Teachers.teach_id == id).count() != 0:
        teacher = session.query(Teachers).filter(Teachers.teach_id == id).first()
        if teacher is None:
            teacher = Teachers(teach_id=id)
        teacher.fullname = name
        session.add(teacher)
    session.commit()
    session.close()
