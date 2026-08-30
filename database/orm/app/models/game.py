from datetime import datetime
from sqlalchemy import DateTime,String,func
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

class Base(DeclarativeBase):
    pass 
class Game(Base):
    __tablename__="games"
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String(255))
    genre:Mapped[str]=mapped_column(String(100))
    platform:Mapped[str]=mapped_column(String(100))
    price:Mapped[int]=mapped_column()
    created_at:Mapped[datetime]=mapped_column(DateTime,server_default=func.now())
    updated_at:Mapped[datetime]=mapped_column(DateTime,server_default=func.now(),onupdate=func.now())

    def __repr__(self):
        return f"Game (id={self.id} title={self.title} platform={self.platform}) "
        
