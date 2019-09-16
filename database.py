from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://contre:secret@localhost:3306/mails')
Session = sessionmaker(bind=engine)

Base = declarative_base()
