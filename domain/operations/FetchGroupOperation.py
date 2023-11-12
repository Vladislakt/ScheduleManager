from typing import Optional
from domain.storage.Group import Group
from domain.storage.GroupRepository import GroupRepository

class FetchClassroomOperation:
    def __init__(self, group_repository: GroupRepository):
        self.group_repository = group_repository

    def fetch(self, nameid: str) -> Optional[Group]:
        return self.group_repository.fetch(nameid)