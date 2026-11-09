from fastapi import APIRouter
from app.database.models import User, db
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def auth():
    return {"message":"auth routes"}

@auth_router.post("/create_account")
async def create_account(email:str,password:str,name:str,language:str):
    Session = sessionmaker(bind=db)
    session = Session()
    user = session.query(User).filter(User.email==email).first()
    if user:
        return {"message":"A user with this email already exists."}
    else:
        new_user = User(name,email,password,language)
        session.add(new_user)
        session.commit()
        return{"message":"User registered successfully"}
    

    