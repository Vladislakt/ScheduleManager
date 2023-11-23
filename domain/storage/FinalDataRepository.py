from domain.storage import FinalData

class FinalDataRepository:
    def __init__(self):
        self.finaldata_list = []

    def add_finaldata(self, finaldata: FinalData):
        self.finaldata_list.append(finaldata)

    def list(self):
        return list(self.finaldata_list.values())

    def fetch(self, day_and_num: int):
        return self.finaldata_list[day_and_num]