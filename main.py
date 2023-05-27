from fastapi import FastAPI
from db import Base, engine
from routers import authentication_router, profile_router, image_router, lesson_router, portfolio_router, course_router
from fastapi.staticfiles import StaticFiles 

app = FastAPI()

app.mount('/uploads', StaticFiles(directory='uploads'), name='uploads')

Base.metadata.create_all(engine)

app.include_router(authentication_router)
app.include_router(profile_router)
app.include_router(image_router)
app.include_router(portfolio_router)
app.include_router(course_router)
app.include_router(lesson_router)
