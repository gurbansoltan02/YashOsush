from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from db import get_db
import crud
from upload_depends import upload_image, delete_uploaded_image

image_router = APIRouter(tags=['Images'])

@image_router.post('/upload-employer-image')
def upload_employer_image(id: int, db: Session = Depends(get_db), file: UploadFile = File(...)):
    try:
        result = crud.create_employer_image(id, file, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)

@image_router.delete('/delete-employer-image/{id}')
def delete_employer_image(id: int, db: Session = Depends(get_db)):
    try:
        result = crud.delete_employer_image(id, db)
        return JSONResponse(status_code=status.HTTP_200_OK, content={'result': 'DELETED'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'result': 'NOT'})


@image_router.post('/upload-employee-image')
def upload_employee_image(id: int, db: Session = Depends(get_db), file: UploadFile = File(...)):
    try:
        result = crud.create_employee_image(id, file, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)

@image_router.delete('/delete-employee-image/{id}')
def delete_employee_image(id: int, db: Session = Depends(get_db)):
    try:
        result = crud.delete_employee_image(id, db)
        return JSONResponse(status_code=status.HTTP_200_OK, content={'result': 'DELETED'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'result': 'NOT'})