from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database.database import Base


# Класс представления отношения lessons
class Lessons(Base):
    __tablename__ = 'lessons'

    # Поля
    id = Column(Integer, primary_key=True, nullable=False)
    teach_id = Column(Integer, ForeignKey('teachers.teach_id', ondelete='CASCADE'))
    group_name = Column(Integer, ForeignKey('groups.group_name', ondelete='CASCADE'))
    quantity = Column(Integer, nullable=False)
    lesson_name = Column(String, nullable=False)
    projector = Column(Boolean, nullable=False)
    computers = Column(Boolean, nullable=False)

    # Создание зависимости
    teachers = relationship("Teachers", back_populates="lesson")
    groups = relationship("Groups", back_populates="lesson")
    cell = relationship('Cell',
                        back_populates="lesson",
                        cascade="all, delete",
                        passive_deletes=True, )

    def __repr__(self):
        return f'Lessons [ID: {self.id}, Препод: {self.teach_id}, Группа: {self.group_name}, Предмет: {self.lesson_name}, Проектор: {self.projector}, Компьютеры: {self.computers}]'
