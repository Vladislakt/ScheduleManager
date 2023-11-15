from domain.storage.Storage import Storage
from domain.storage import ClassroomRepository
from domain.storage import FinalDataRepository
from domain.storage import GroupRepository
from domain.storage import LessonRepository
from domain.storage import TeacherRepository
from domain.operations import FetchClassroomOperation, FetchGroupOperation, FetchLessonOperation, FetchFinalDataOperation, FetchTeacherOperation
from domain.operations import ListGroupOperation, ListClassroomOperation, ListTeacherOperation, ListLessonOperation, ListFinalDataOperation
from domain.operations import AddGroupOperation, AddClassroomOperation, AddTeacherOperation, AddLessonOperation, AddFinalDataOperation

class OperationStorage:
    def __init__(self, storage: Storage):
        self.fetchClassroomOperation = FetchClassroomOperation(storage.classroom_repository)
        self.fetchFinalDataOperation = FetchFinalDataOperation(storage.finaldata_repository)
        self.fetchGroupOperation = FetchGroupOperation(storage.group_repository)
        self.fetchLessonOperation = FetchLessonOperation(storage.lesson_repository)
        self.fetchTeacherOperation = FetchTeacherOperation(storage.teacher_repository)
        self.listClassroomOperation = ListClassroomOperation(storage.classroom_repository)
        self.listFinalDataOperation = ListFinalDataOperation(storage.finaldata_repository)
        self.listGroupOperation = ListGroupOperation(storage.group_repository)
        self.listLessonOperation = ListLessonOperation(storage.lesson_repository)
        self.listTeacherOperation = ListTeacherOperation(storage.teacher_repository)
        self.addClassroomOperation = AddClassroomOperation(storage.classroom_repository)
        self.addFinalDataOperation = AddFinalDataOperation(storage.finaldata_repository)
        self.addGroupOperation = AddGroupOperation(storage.group_repository)
        self.addLessonOperation = AddLessonOperation(storage.lesson_repository)
        self.addTeacherOperation = AddTeacherOperation(storage.teacher_repository)

