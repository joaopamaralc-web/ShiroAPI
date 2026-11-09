from sqlalchemy import create_engine, Column,String,Integer,Boolean
from sqlalchemy.orm import declarative_base
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_URL = f"sqlite:///{BASE_DIR / 'database.db'}"
db = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column("id",Integer,autoincrement=True,primary_key=True)
    username = Column("username",String)
    email = Column("email",String)
    password = Column("password",String)
    admin = Column("admin",Boolean)
    language = Column("language",String)

    def __init__(self,username,email,password,language,admin=False):
        self.username = username
        self.email = email
        self.password = password
        self.language = language
        self.admin = admin

