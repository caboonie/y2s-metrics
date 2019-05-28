from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    password = Column(String)
    username = Column(String)

    def __str__(self):
        return str(self.id)+": "+self.username

class Metric(Base):
    __tablename__ = "metrics"
    id = Column(Integer, primary_key=True)
    action = Column(String)
    version = Column(String)
    timestamp = Column(DateTime)
    user = Column(String)

    def __str__(self):
        return str(self.id)+": "+self.user+" "+self.version+" "+self.timestamp+" "+self.action
