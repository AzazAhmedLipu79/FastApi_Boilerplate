# Here we will define out tables and there model🏓
from enum import Enum

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,Enum as EnumType

from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .db_connection import Base

class Gender(Enum):
    M = 'Male'
    F = 'Female'
    OTHER = 'Other'

class Role(Enum):
    member='member'
    moderator = 'moderator'
    admin = 'admin'


class User(Base):
    __tablename__="users"
    userId = Column(Integer, primary_key=True, nullable=False)
    userName = Column(String(41), nullable=False)
    bornDate = Column(String(41), nullable=False)
    email = Column(String(41), nullable=False, unique=True)
    password = Column(String, nullable=False)    
    gender = Column(EnumType(Gender), nullable=False)
    role = Column(EnumType(Role), nullable=False, server_default="member")

""" 
The provided code defines three Enum classes called Gender, Role, and User. The Gender class defines three values for the possible genders, while the Role class defines three different roles. The User class defines a table schema for a user table using SQLAlchemy's Column objects. The schema includes columns for userId, userName, bornDate, email, password, gender, and role.

The gender column is defined as an enumerated type using the EnumType class with the Gender class as its argument. This means that the gender column will only accept values that are members of the Gender Enum. Similarly, the role column is also defined as an enumerated type using the EnumType class with the Role class as its argument.

Overall, this code defines a database schema that describes a user table, where each user is associated with a gender and a role. """



class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")


# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, nullable=False)
#     email = Column(String, nullable=False, unique=True)
#     password = Column(String, nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True),
#                         nullable=False, server_default=text('now()'))


class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), primary_key=True)