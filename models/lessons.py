from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database.database import Base


# Класс представления отношения lessons
class Lessons(Base):
    __tablename__ = 'lessons'

    # Поля
    id = Column(Integer, primary_key=True, nullable=False)
    teach_id = Column(Integer, ForeignKey('teachers.teach_id'))
    group_name = Column(Integer, ForeignKey('groups.group_name'))
    lesson_name = Column(String, nullable=False)
    projector = Column(Boolean, nullable=False)
    computers = Column(Boolean, nullable=False)

    # Создание зависимости
    finaldata = relationship('FinalData')
