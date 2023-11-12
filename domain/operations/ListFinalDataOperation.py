from typing import List
from domain.storage.FinalData import FinalData
from domain.storage.FinalDataRepository import FinalDataRepository


class ListFinalDataOperation:
    def __init__(self, finaldata_repository: FinalDataRepository):
        self.finaldata_repository = finaldata_repository

    def list(self) -> List[FinalData]:
        return self.finaldata_repository.list()