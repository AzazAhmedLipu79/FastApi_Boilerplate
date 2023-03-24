from fastapi import APIRouter, Depends, status, HTTPException, Response
from app.db.db_connection import get_db
from app.db.table_models import User
from ..Schemas import UserRegistration, UserRegistration_Response
from sqlalchemy.orm import Session 
from ...Utils.utilities import hashPass


router = APIRouter(prefix="/auth",tags=['Registration'])


@router.post('/registration', status_code= status.HTTP_201_CREATED, response_model= UserRegistration_Response)
def createNewUser(user : UserRegistration, db: Session = Depends(get_db)):
    
    # hash the password - user.password
    hashed_password = hashPass(user.password)
    user.password = hashed_password

    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return user
""" 
This code defines a FastAPI endpoint to handle user registration requests using HTTP POST. The endpoint accepts a user object, which contains information about the user being registered, such as their name, email, and password.

Before creating a new user, the password specified in the user object is hashed using an unknown hashPass() function. The hashed password is then assigned to the password attribute of the user object.

A new User object is then created using the values in the user object by unpacking them using the double-asterisk notation (**user.dict()). This new User object is then added to the database session (db.add(new_user)), committed to persist the changes (db.commit()), and then refreshed to ensure it has the most up-to-date values (db.refresh(new_user)). """