from sqlalchemy import Column, Integer, String
from autop.database import Base


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)
    type = Column(String(120), unique=False)
    summary = Column(String(120), unique=False)

    def __init__(self, name=None, summary=None, type=None):
        self.name = name
        self.type = type
        self.summary = summary

    def __repr__(self):
        return f'<Car {self.name}>'
