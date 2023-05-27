from pydantic import BaseModel

class loginSchema(BaseModel):
    email: str 
    password: str 

class registerSchema(loginSchema):
    user_type: int 
    username: str 

class profileSchemaEmployer(BaseModel):
    user_id: int
    full_name: str
    description: str

class profileSchemaEmployee(profileSchemaEmployer):
    phone_number: str

class courseSchema(BaseModel):
    name: str
