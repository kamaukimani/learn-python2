
from model import Dog,engine,session
from model import Base


def create_table(Base):
    Base.metadata.create_all(engine)
def save(session,dog):
    session.add(dog)
    session.commit()
def get_all(session):
    dogs=session.query(Dog).all()
    return dogs
def find_by_name(session,name):
    dog=session.query(Dog).filter(Dog.name == name).first()
    return dog
def find_by_id(session,id):
    dog=session.query(Dog).filter(Dog.id == id).first()
    return dog
def find_by_name_and_breed(session,name,breed):
    dog=session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return dog
def update_breed(session,dog,breed):

    dog.breed=breed
    session.commit()

#create_table(Base)
dog4=Dog(
    name="Soldier",
    breed="German Shepherd"
)
save(session,dog4)
# dog=session.query(Dog).filter(Dog.id == 4).first()

# session.delete(dog)
# session.commit()
# print(dog)
print(get_all(session))
print(find_by_name(session,"Lex"))
print(find_by_id(session,2))
print(find_by_name_and_breed(session,"Tusker","German Shepherd"))
print(dog4)
print(update_breed(session,dog4,"Bulldog"))