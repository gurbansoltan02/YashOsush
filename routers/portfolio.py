from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from db import get_db
import crud
from upload_depends import upload_portfolio, delete_uploaded_portfolio

portfolio_router = APIRouter(tags=['Portfolio'])

@portfolio_router.post('/upload-portfolio')
def upload_portfolio(id: int, db: Session = Depends(get_db), file: UploadFile = File(...)):
    try:
        result = crud.create_portfolio(id, file, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)

@portfolio_router.delete('/delete-portfolio/{id}')
def delete_portfolio(id: int, db: Session = Depends(get_db)):
    try:
        result = crud.delete_portfolio(id, db)
        return JSONResponse(status_code=status.HTTP_200_OK, content={'result': 'DELETED'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'result': 'NOT'})