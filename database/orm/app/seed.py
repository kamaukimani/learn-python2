from faker import Faker 
import random
from sqlalchemy import create_engine,func,select
from sqlalchemy.orm import sessionmaker
from models.game import Game
 
faker=Faker()

if __name__=="__main__":
    engine=create_engine("sqlite:///game.db")
    Session=sessionmaker(bind=engine)
    session=Session()

    session.query(Game).delete()
    session.commit()

    print("Seeding games...........")
    games=[
        Game(
            title=faker.name(),
            genre=faker.word(),
            platform=faker.word(),
            price=random.randint(0, 60)
        )
        for i in range(50)
    ]
    session.add_all(games)
    session.commit()
    #print(session.scalar(select(func.count(Game.id))))