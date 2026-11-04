from sqlalchemy import create_engine, Column,String,Integer,Boolean
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///database.db")
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column("id",Integer,autoincrement=True,primary_key=True)
    username = Column("username",String)
    email = Column("email",String)
    password = Column("password",String)
    admin = Column("admin",Boolean)
    idiom = Column("idiom",String)