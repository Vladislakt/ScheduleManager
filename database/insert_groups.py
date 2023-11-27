from database.create_session import create_session
from models.groups import Groups


# Функция для изначального заполнения отношения groups
def insert_groups(filename, group_list):
    session = create_session(filename)
    for element in group_list:
        group = Groups(group_name=element[0], size=element[1])
        session.add(group)
    session.commit()
    session.close()
