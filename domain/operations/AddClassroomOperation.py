from domain.storage.Classroom import Classroom
from domain.storage.ClassroomRepository import ClassroomRepository

class AddClassroomOperation:
    def __init__(self, classroom_repository: ClassroomRepository):
        self.classroom_repository = classroom_repository

    def add_classroom(self, classroom: Classroom):
        self.classroom_repository.classroom_list.append(classroom)