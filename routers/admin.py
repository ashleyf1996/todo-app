from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, Path
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from models import Todos
from database import engine, SessionLocal
from starlette import status
from models import Users
from .auth import get_current_user

router = APIRouter(
    prefix='/admin', 
    tags=['admin']
)

#models.Base.metadata.create_all(bind=engine) 


def get_db():
    db = SessionLocal() #contact db
    try:
        yield db
    finally:
        db.close() #executing after response is delivered to close 

db_dependency = Annotated[Session, Depends(get_db)] # dependacy injection depends means to do something beofre this code. ie relies on DB being open
user_dependency = Annotated[dict, Depends(get_current_user)]




@router.get("/todo", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None or user.get("user_role") != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(Todos).all()


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user:user_dependency, db: db_dependency, todo_id = Path(gt=0)):

    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None: 
        raise HTTPException(status_code=404, detail='Todo not found')
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()