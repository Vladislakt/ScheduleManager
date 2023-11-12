from dataclasses import dataclass

@dataclass
class Lesson:
    id: int
    teacher_id: int
    group_name: str
    lesson_name: str
    quantity: int
    projector: bool
    computers: bool
