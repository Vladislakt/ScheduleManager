class ClassroomRepository:
    def __init__(self):
        self.classroom_list = []

    def add_teacher(self, classroom):
        self.classroom_list.append(classroom)