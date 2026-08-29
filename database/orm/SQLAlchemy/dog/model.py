from sqlalchemy import Integer,String,create_engine
from sqlalchemy.orm import DeclarativeBase,Session,Mapped,mapped_column

class Base(DeclarativeBase):
    pass

class Dog(Base):
    __tablename__="dogs"
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    name:Mapped[str]=mapped_column(String,unique=True)
    breed:Mapped[str]=mapped_column(String)

    def __repr__(self):
        return f"Dog {self.id}:{self.name}, {self.breed}"

# if __name__=="__main__":
#     engine=create_engine("sqlite:///dog.db")
#     Base.metadata.create_all(engine)
#     session=Session(engine)

engine=create_engine("sqlite:///dog.db")
session=Session(engine)