from domain.storage.FinalData import FinalData
from domain.storage.FinalDataRepository import FinalDataRepository

class AddFinalDataOperation:
    def __init__(self, finaldata_repository: FinalDataRepository):
        self.finaldata_repository = finaldata_repository

    def add_finaldata(self, finaldata: FinalData):
        self.finaldata_repository.finaldata_list.append(finaldata)