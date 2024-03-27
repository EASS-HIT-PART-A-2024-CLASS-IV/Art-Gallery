from pydantic import BaseModel, Field, validator, field_validator
from app.exceptions import *


class UserBaseRequestModel(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

    @field_validator('password')
    def password_length(cls, v):
        if len(v) < 6:
            raise PasswordTooShort('Password must be at least 6 characters')
        if len(v) > 50:
            raise PasswordTooLong('Password must be at most 50 characters')
        return v
    
    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 3:
            raise UsernameTooShort('Username must be at least 3 characters')
        if len(v) > 50:
            raise UsernameTooLong('Username must be at most 50 characters')
        return v
        
    class Config:
        schema_extra = {
            "example": {
                "username": "johndoe",
                "password": "securepassword123"
            }
        }


class UserInternalRequestModel(BaseModel):
    username: str
    password: bytes # This is the hashed password


