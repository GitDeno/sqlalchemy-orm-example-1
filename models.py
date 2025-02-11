import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

from session import engine

Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    user_name = Column(String(50), unique=True, nullable=False)
    salary = Column(Float, default=0)
    email = Column(String(50), unique=True, nullable=False)
    registration_date = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f"User({self.user_name})"
