from datetime import datetime
from sqlalchemy import create_engine,DateTime,Integer,String,CheckConstraint,desc,asc,func
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,sessionmaker  #Session
from faker import Faker

class Base(DeclarativeBase):
    pass
class Student(Base):
    __tablename__="students"
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    name:Mapped[str]=mapped_column(String)
    email:Mapped[str]=mapped_column(String(55),unique=True)
    marks:Mapped[int]=mapped_column(Integer,CheckConstraint("marks BETWEEN 1 AND 12"))
    birthday:Mapped[datetime]=mapped_column(DateTime)
    enrolled_date:Mapped[datetime]=mapped_column(DateTime,default=datetime.now)

    def __repr__(self):
        return f"Student {self.id}:{self.name}, Grade:{self.grade}"

engine=create_engine("sqlite:///student.db")