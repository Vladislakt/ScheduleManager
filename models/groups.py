from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base


# Класс представления отношения groups
class Groups(Base):
    __tablename__ = 'groups'

    # Поля
    group_name = Column(String, primary_key=True, nullable=False)
    size = Column(Integer, nullable=False)

    # Создание зависимости
    lessons = relationship('Lessons')

    def __repr__(self):
        return f'Groups [Группа: {self.group_name}, Размер: {self.size}]'
