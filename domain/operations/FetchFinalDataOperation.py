from typing import Optional
from domain.storage.FinalData import FinalData
from domain.storage.FinalDataRepository import FinalDataRepository

class FetchFinalDataOperation:
    def __init__(self, finaldata_repository: FinalDataRepository):
        self.finaldata_repository = finaldata_repository

    def fetch(self, day_and_num: int) -> Optional[FinalData]:
        return self.finaldata_repository.fetch(day_and_num)