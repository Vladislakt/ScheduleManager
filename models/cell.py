from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


# Класс представления отношения cell
class Cell(Base):
    __tablename__ = 'cell'

    # Поля
    day = Column(String, primary_key=True, nullable=False)
    group = Column(String, primary_key=True, nullable=False)
    number_of_class = Column(Integer, primary_key=True, nullable=False)
    lesson_id = Column(Integer, ForeignKey('lessons.id', ondelete='CASCADE'))
    classroom = Column(String, ForeignKey('classrooms.class_number', ondelete='CASCADE'))

    classroom_table = relationship("Classrooms", back_populates="cell")
    lesson = relationship("Lessons", back_populates="cell")

    def __init__(self, group, day, number_of_class, lesson_id, classroom):
        super().__init__()
        self.day = day
        self.group = group
        self.number_of_class = number_of_class
        self.lesson_id = lesson_id
        self.classroom = classroom

    def __repr__(self):
        return f'Cell [День: {self.day}, Группа: {self.group}, Номер пары: {self.number_of_class}' \
               f' Пара: {self.lesson_id}, Кабинет: {self.classroom}]'
