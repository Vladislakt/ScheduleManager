from typing import List
from domain.storage.Group import Group
from domain.storage.GroupRepository import GroupRepository


class ListGroupOperation:
    def __init__(self, group_repository: GroupRepository):
        self.group_repository = group_repository

    def list(self) -> List[Group]:
        return self.group_repository.list()