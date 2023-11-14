from sqlalchemy import Column, Integer, String, ForeignKey

from DataBase.database import Base


# Класс представления отношения finaldata
class FinalData(Base):
    __tablename__ = 'finaldata'

    # Поля
    day_and_num = Column(Integer, primary_key=True, nullable=False)
    lesson_id = Column(Integer, ForeignKey('lessons.id'))
    class_number = Column(String, ForeignKey('classrooms.class_number'))

    def __repr__(self):
        return f'FinalData [День/Пара: {self.day_and_num}, Пара: {self.lesson_id}, Кабинет: {self.class_number}]'
