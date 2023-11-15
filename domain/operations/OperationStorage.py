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
    def init(self, storage: Storage):
        self.fetchClassroomOperation = FetchClassroomOperation(ClassroomRepository)
        self.fetchFinalDataOperation = FetchFinalDataOperation(FinalDataRepository)
        self.fetchGroupOperation = FetchGroupOperation(GroupRepository)
        self.fetchLessonOperation = FetchLessonOperation(LessonRepository)
        self.fetchTeacherOperation = FetchTeacherOperation(TeacherRepository)
        self.listClassroomOperation = ListClassroomOperation(ClassroomRepository)
        self.listFinalDataOperation = ListFinalDataOperation(FinalDataRepository)
        self.listGroupOperation = ListGroupOperation(GroupRepository)
        self.listLessonOperation = ListLessonOperation(LessonRepository)
        self.listTeacherOperation = ListTeacherOperation(TeacherRepository)
        self.addClassroomOperation = AddClassroomOperation(ClassroomRepository)
        self.addFinalDataOperation = AddDataOperation(FinalDataRepository)
        self.addGroupOperation = AddGroupOperation(GroupRepository)
        self.addLessonOperation = AddLessonOperation(LessonRepository)
        self.addTeacherOperation = AddTeacherOperation(TeacherRepository)

