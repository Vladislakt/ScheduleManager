class GroupRepository:
    def __init__(self):
        self.group_list = []

    def add_teacher(self, group):
        self.group_list.append(group)