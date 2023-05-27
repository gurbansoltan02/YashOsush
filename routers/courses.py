from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session 
from db import get_db
import crud 
from models import courseSchema

course_router = APIRouter(tags=['Course'])

@course_router.post('/add-course')
def add_course(req: courseSchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_course(req, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong!')

@course_router.get('/get-course')
def get_course(db: Session = Depends(get_db)):
    try:
        result = crud.read_course(db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong!')