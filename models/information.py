from sqlalchemy import Column, Boolean, Integer

from database.database import Base


# Класс представления отношения information
class Information(Base):
    __tablename__ = 'information'

    # Поля
    isSaturday = Column(Boolean, primary_key=True, nullable=False)
    maxLesson = Column(Integer, primary_key=True, nullable=False)

    def __repr__(self):
        return f'Information [isSaturday: {self.name}; maxLesson: {self.maxLesson}]'
