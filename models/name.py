from sqlalchemy import Column, String

from DataBase.database import Base


# Класс представления отношения lessons
class Name(Base):
    __tablename__ = 'name'

    # Поля
    name = Column(String, primary_key=True, nullable=False)

    def __repr__(self):
        return f'Name [name: {self.name}]'
