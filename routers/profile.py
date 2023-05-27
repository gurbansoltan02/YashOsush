from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session 
from db import get_db
import crud 
from models import profileSchemaEmployer, profileSchemaEmployee, EmployerProfile, EmployeeProfile

profile_router = APIRouter(tags=['Profile'])

@profile_router.post('/add-employer-profile')
def add_employer_profile(req: profileSchemaEmployer, db: Session = Depends(get_db)):
    try:
        result = crud.create_employer_profile(req, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong!')

@profile_router.get('/get-employer-profile')
def get_employer_profile(db: Session = Depends(get_db)):
    try:
        result = crud.read_employer_profile(db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong!')



@profile_router.post('/add-employee-profile')
def add_employee_profile(req: profileSchemaEmployee, db: Session = Depends(get_db)):
    try:
        result = crud.create_employee_profile(req, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong!')

@profile_router.get('/get-employee-profile')
def get_employee_profile(db: Session = Depends(get_db)):
    try:
        result = crud.read_employee_profile(db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong!')