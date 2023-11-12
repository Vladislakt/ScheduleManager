from dataclasses import dataclass

@dataclass
class Classroom:
    classroom_id: str
    max_size: int
    projector: bool
    computers: int
