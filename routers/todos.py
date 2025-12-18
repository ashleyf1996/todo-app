from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, Path
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from models import Todos
from database import engine, SessionLocal
from starlette import status

router = APIRouter()

#models.Base.metadata.create_all(bind=engine) 


def get_db():
    db = SessionLocal() #contact db
    try:
        yield db
    finally:
        db.close() #executing after response is delivered to close 

db_dependency = Annotated[Session, Depends(get_db)] # dependacy injection depends means to do something beofre this code. ie relies on DB being open

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str  = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool


@router.get("/", status_code= status.HTTP_200_OK) 
async def read_all(db: db_dependency): 
    return db.query(Todos).all()


@router.get("/todo/{todo_id}", status_code= status.HTTP_200_OK) 
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first() #sql query. first return as soon as you get a match dont need to look through 
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found')
    

@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.model_dump())
    db.add(todo_model) #getting db ready
    db.commit() #actualy doing it 


@router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency, 
                      todo_request: TodoRequest,
                       todo_id: int  = Path(gt=0)):    
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, 
                     # todo_request: TodoRequest,
                       todo_id: int  = Path(gt=0)):    
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()



