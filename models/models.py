from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    user_type = Column(Integer, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    employer = relationship('EmployerProfile', back_populates='user1')
    employee = relationship('EmployeeProfile', back_populates='user2')
    

class EmployerProfile(Base):
    __tablename__ = 'employer_profile'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    full_name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user1 = relationship('Users', back_populates='employer')
    image = relationship('EmployerImage', back_populates='employer')

    
class EmployerImage(Base):
    __tablename__ = 'employer_images'
    id = Column(Integer, primary_key=True, index=True)
    img = Column(String, nullable=False)
    employer_id = Column(Integer, ForeignKey('employer_profile.id'))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    employer = relationship('EmployerProfile', back_populates='image')


class EmployeeProfile(Base):
    __tablename__ = 'employee_profile'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    full_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    description = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user2 = relationship('Users', back_populates='employee')
    image = relationship('EmployeeImage', back_populates='employee')
    portfolio = relationship('Portfolio', back_populates='employee')

class EmployeeImage(Base):
    __tablename__ = 'employee_images'
    id = Column(Integer, primary_key=True, index=True)
    img = Column(String, nullable=False)
    employee_id = Column(Integer, ForeignKey('employee_profile.id'))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    employee = relationship('EmployeeProfile', back_populates ='image')

class Portfolio(Base):
    __tablename__ = 'portfolio'
    id = Column(Integer, primary_key=True, index=True)
    file = Column(String)
    employee_id = Column(Integer, ForeignKey('employee_profile.id'))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    employee = relationship('EmployeeProfile', back_populates='portfolio')

class Courses(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    lessons = relationship('Lessons', back_populates='courses')

class Lessons(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True, index=True)
    lesson = Column(String, nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    courses = relationship('Courses', back_populates='lessons')

