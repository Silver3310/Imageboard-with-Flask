from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgres://sctqiewhhnvmer:74536945114a692e0b2c696d4824b5500cc9e1d8b0fdfaa08b3b746a6e8484e1@ec2-54-221-236-144.compute-1.amazonaws.com:5432/d2qcqv9deiss32"

db = create_engine(db_string)

base = declarative_base()


class Fruit(base):
    __tablename__ = 'fruits'

    name = Column(String, primary_key=True)
    color = Column(String)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

firstfruit = Fruit(
    name='apple',
    color='yellow'
)
session.add(firstfruit)
session.commit()

fruits = session.query(Fruit)
for fruit in fruits:
    print(fruit.name)

session.delete(firstfruit)
session.commit()

Fruit.__table__.drop(db)
