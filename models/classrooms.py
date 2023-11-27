from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from database.database import Base


# Класс представления отношения classrooms
class Classrooms(Base):
    __tablename__ = 'classrooms'

    # Поля
    class_number = Column(String, primary_key=True, nullable=False)
    max_size = Column(Integer, nullable=False)
    projector = Column(Boolean, nullable=False)
    computers = Column(Integer, nullable=False)

    # Создание зависимости
    finaldata = relationship('FinalData')

    def __repr__(self):
        return f'Classrooms [Кабинет: {self.class_number}, Размер: {self.max_size}, Проектор: {self.projector}, Компьютеры: {self.computers}]'
