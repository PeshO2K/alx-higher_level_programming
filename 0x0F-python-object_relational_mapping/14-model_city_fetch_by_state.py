#!/usr/bin/python3
"""List all States Module"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Fetch All """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    for city, state in session.query(City, State).filter(
         City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
