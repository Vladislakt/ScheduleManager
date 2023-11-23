from domain.storage.Group import Group
from domain.storage.GroupRepository import GroupRepository

class AddGroupOperation:
    def __init__(self, group_repository: GroupRepository):
        self.group_repository = group_repository

    def add_group(self, group: Group):
        self.group_repository.group_list.append(group)