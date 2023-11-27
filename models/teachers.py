from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base


# Класс представления отношения teachers
class Teachers(Base):
    __tablename__ = 'teachers'

    # Поля
    teach_id = Column(Integer, primary_key=True, nullable=False)
    fullname = Column(String, nullable=False)

    # Создание зависимости
    lesson = relationship('Lessons')

    def __repr__(self):
        return f'Teachers [ID: {self.teach_id}, ФИО: {self.fullname}]'
