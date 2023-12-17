#!/usr/bin/python3
"""List all States Module"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Fetch All """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    state = session.query(State).filter_by(
         name=sys.argv[4]).first()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")
    session.close()
