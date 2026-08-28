# import sqlalchemy
# print(sqlalchemy.__version__)
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
    grade:Mapped[int]=mapped_column(Integer,CheckConstraint("grade BETWEEN 1 AND 12"))
    birthday:Mapped[datetime]=mapped_column(DateTime)
    enrolled_date:Mapped[datetime]=mapped_column(DateTime,default=datetime.now)

    def __repr__(self):
        return f"Student {self.id}:{self.name}, Grade:{self.grade}"


if __name__=="__main__":
    engine=create_engine("sqlite:///student.db")
    Base.metadata.create_all(engine)
    Session=sessionmaker(bind=engine)
    session=Session()

    albert_einstein=Student(
        name="Albert Einstein",
        email="albert.einstein@zerich.edu",
        grade=6,
        birthday=datetime(
            year=1879,
            month=3,
            day=14
        ),
    )
    alan_turing=Student(
        name="Alan Turing",
        email="alan.turing@sherborne.edu",
        #grade=13,
        grade=11,
        birthday=datetime(
            year=1912,
            month=6,
            day=23
        ),
    )
    # session.add_all([albert_einstein,alan_turing])
    # session.commit()

    # students=session.query(Student)
    # print([student for student in students])
    students=session.query(Student).all()
    print(students)
    names=[name for name in session.query(Student.name)]
    print(names)
    students_by_name=[student for student in session.query(Student.name).order_by(Student.name)]
    print(students_by_name)
    students_by_grade=[student for student in session.query(Student.name,Student.grade).order_by(desc(Student.grade))]
    print(students_by_grade)
    # oldest=[student for student in session.query(Student.name,Student.birthday).order_by(asc(Student.birthday)).limit(1)]
    # print(f"The oldest student:{oldest}")
    oldest=[student for student in session.query(Student.name,Student.birthday).order_by(asc(Student.birthday)).first()]
    print(f"The oldest student:{oldest}")
    faker=Faker()
    # student1=Student(
    #     name=faker.name(),
    #     email=faker.email(),
    #     grade=faker.random_int(min=1,max=12),
    #     birthday=faker.date_of_birth()
    # )
    # session.add(student1)
    # session.commit()

    # student2=Student(
    #     name=faker.name(),
    #     email=faker.email(),
    #     grade=faker.random_int(min=1,max=12),
    #     birthday=faker.date_of_birth()
    # )
    # student3=Student(
    #     name=faker.name(),
    #     email=faker.email(),
    #     grade=faker.random_int(min=1,max=12),
    #     birthday=faker.date_of_birth()
    # )
    # session.add_all([student2,student3])
    # session.commit()

    # smith=session.query(Student).filter(Student.name == "Russell Smith").first()
    # print(smith)
    # smith.name="Smith"
    # session.commit()
    # carla=session.query(Student).filter(Student.email == "andrea18@example.com").first()
    # print([carla])
    # session.delete(carla)
    # session.commit()
    # session.query(Student).filter(Student.name == "Samuel").update({
    #     Student.name: "David"
    # })
    # session.commit()
    session.query(Student).update({
        Student.email:func.replace(
            Student.email,
            "@example.org",
            "@gmail.com"
        )
    })
    session.commit()

