from dataclasses import dataclass
from domain.storage import Classroom
from domain.storage import FinalData
from domain.storage import Group
from domain.storage import Lesson
from domain.storage import Teacher
from domain.storage import ClassroomRepository
from domain.storage import FinalDataRepository
from domain.storage import GroupRepository
from domain.storage import LessonRepository
from domain.storage import TeacherRepository

@dataclass
class Storage:
    classroom_repository: ClassroomRepository
    group_repository: GroupRepository
    lesson_repository: LessonRepository
    teacher_repository: TeacherRepository
    finaldata_repository: FinalDataRepository

    def initRepositoryStorage(self):
        classroom212 = Classroom(
            classroom_id = "212",
            max_size = 60,
            projector = True,
            computers = 30
        )
        classroom220 = Classroom(
            classroom_id = "220",
            max_size = 120,
            projector = True,
            computers = 0
        )
        classroom_repository = ClassroomRepository(classroom212, classroom220)

        group31 = Group(
            nameid = "IVT-31",
            size = 24
        )
        group32 = Group(
            nameid = "IVT-32",
            size = 26
        )
        group_repository = GroupRepository(group31, group32)

        lesson_codeengi = Lesson(
            id = 0,
            teacher_id = 0,
            group_name = "IVT-31",
            lesson_name = "Программная Инженерия",
            quantity = 4,
            projector = True,
            computers = False
        )
        lesson_inddev = Lesson(
            id = 1,
            teacher_id = 1,
            group_name = "IVT-32",
            lesson_name = "Промышленная Разработка",
            quantity = 5,
            projector = False,
            computers = True
        )
        lesson_repository = LessonRepository(lesson_codeengi, lesson_inddev)

        teacher_fedulov = Teacher(
            teacher_id = 0,
            fullname = "Федулов Даниил Неизвестнович"
        )
        teacher_poletaev = Teacher(
            teacher_id = 0,
            fullname = "Полетаев Анатолий Юрьевич"
        )
        teacher_repository = TeacherRepository(teacher_fedulov, teacher_poletaev)

        finaldata_monday = FinalData(
            classroom_idnum = "212",
            lesson_id = 0,
            day_and_num = 11
        )
        finaldata_tuesday = FinalData(
            classroom_idnum = "220",
            lesson_id = 1,
            day_and_num = 21
        )
        finaldata_repository = FinalDataRepository(finaldata_monday, finaldata_tuesday)

        return Storage(classroom_repository,
                        group_repository,
                        lesson_repository,
                        teacher_repository,
                        finaldata_repository)
