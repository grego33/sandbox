from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine that stores data in an in-memory SQLite database
engine = create_engine('sqlite:///:memory:', echo=True)

# Create a base class for our classes definitions
Base = declarative_base()

# Define the Car class
class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)

    def __repr__(self):
        return f"<Car(make='{self.make}', model='{self.model}', year='{self.year}')>"

# Create the cars table
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Create new Car objects
car1 = Car(make='Toyota', model='Corolla', year=2020)
car2 = Car(make='Honda', model='Civic', year=2019)

# Add the Car objects to the session
session.add(car1)
session.add(car2)

# Commit the session to the database
session.commit()

# Query the database
cars = session.query(Car).all()
for car in cars:
    print(car)