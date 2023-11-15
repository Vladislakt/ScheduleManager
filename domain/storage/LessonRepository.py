class LessonRepository:
    def __init__(self):
        self.lesson_list = []

    def add_teacher(self, lesson):
        self.lesson_list.append(lesson)