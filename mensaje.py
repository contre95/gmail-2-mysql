from sqlalchemy import Column, String, Integer, Date
from base import Base, Session

db_session = Session()
# Extending Model with de Create operation
class CRUD():
     def save(self):
         db_session.add(self)
         try:
             return db_session.commit()
         except Exception as e:
             print(e)    

class Message(Base, CRUD):
    __tablename__ = 'devops_mail'
    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    sender = Column(String, nullable=False, unique=True)
    date = Column(Date)

    def __init__(self,sender, date, subject):
        self.subject = subject
        self.sender = sender
        self.date = date
