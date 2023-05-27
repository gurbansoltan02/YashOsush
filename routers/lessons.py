from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from db import get_db
import crud
from upload_depends import upload_lesson, delete_uploaded_lesson

lesson_router = APIRouter(tags=['Lessons'])


@lesson_router.post('/add-lesson')
def add_lesson(id: int, db: Session = Depends(get_db), file: UploadFile = File(...)):
    try:
        result = crud.create_lesson(id, file, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)


@lesson_router.get('/get-lesson')
def get_lesson(
    page: int,
    limit: int,   
    db: Session = Depends(get_db)
):
    try:
        result = crud.read_lesson(page, limit, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'result': 'Something went wrong'})


@lesson_router.delete('/delete-lesson/{id}')
def delete_lesson(id: int, db: Session = Depends(get_db)):
    try:
        result = crud.delete_lesson(id, db)
        return JSONResponse(status_code=status.HTTP_200_OK, content={'result': 'DELETED'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'result': 'NOT'})
