from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import base

class Blog(base):
    __tablename__ = "blog_details"
    id = Column(Integer , index=True, primary_key=True)
    title = Column(String(255))
    body = Column(String(255))
    userId = Column(Integer , ForeignKey('user_details.id'))
    creator = relationship('User' , back_populates="blogs")


class User(base):
    __tablename__ = "user_details"
    id = Column(Integer , index=True, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    blogs = relationship('Blog' , back_populates="creator")