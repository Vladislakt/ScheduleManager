from domain.storage import Group

class GroupRepository:
    def __init__(self):
        self.group_list = []

    def add_group(self, group: Group):
        self.group_list.append(group)

    def list(self):
        return list(self.group_list.values())

    def fetch(self, nameid: int):
        return self.group_list[nameid]