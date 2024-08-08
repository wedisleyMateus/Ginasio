from sqlalchemy import String, Integer, Float, Column
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(150), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(Integer, nullable=False)
