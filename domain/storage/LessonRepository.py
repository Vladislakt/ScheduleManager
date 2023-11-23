from domain.storage import Lesson

class LessonRepository:
    def __init__(self):
        self.lesson_list = []

    def add_lesson(self, lesson: Lesson):
        self.lesson_list.append(lesson)

    def list(self):
        return list(self.lesson_list.values())

    def fetch(self, id: int):
        return self.lesson_list[id]