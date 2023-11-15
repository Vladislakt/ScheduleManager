from domain.storage import Classroom


class ClassroomRepository:
    def __init__(self):
        self.classroom_list = []

    def add_classroom(self, classroom: Classroom):
        self.classroom_list.append(classroom)

    def list(self):
        return list(self.classroom_list.values())

    def fetch(self, classroom_id: int):
        return self.classroom_list[classroom_id]

