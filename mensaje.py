from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import validates
from database import Base, Session
import re

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
    sender = Column(String, nullable=False)
    date = Column(Date)

    def __init__(self,sender, date, subject):
        self.subject = subject
        self.sender = sender
        self.date = date
    
    @validates('sender')
    def validate_sender(self, key, sender):
        if not sender or (len(sender) == 0):
            raise AssertionError('No correct sender provided')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", sender):
            raise AssertionError('Provided sender is not an email address')
        return sender

    @validates('subject')
    def validate_subject(self, key, subject):
        if not subject or (len(subject) == 0):
            raise AssertionError('No subject provided')
        if len(subject) > 250:
            raise AssertionError("Subject can't have more than 250 characters")
        return subject

