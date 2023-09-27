from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__='users'

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False)
    email=Column(String, nullable=False)
    password=Column(String, nullable=False)

    blogs=relationship("Blog", back_populates="users")

class Blog(Base):  
    __tablename__='blogs'

    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    body=Column(String)
    user_id=Column(Integer, ForeignKey("users.id"))

    creator=relationship("User", back_populates="blogs")


    


