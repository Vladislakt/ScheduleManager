from sqlalchemy import Column, Integer, ForeignKey

from database.database import Base


# Класс представления отношения finaldata
class FinalData(Base):
    __tablename__ = 'finaldata'

    # Поля
    day_and_num = Column(Integer, primary_key=True, nullable=False)
    lesson_id = Column(Integer, ForeignKey('lessons.id'))
    class_number = Column(Integer, ForeignKey('classrooms.class_number'))
