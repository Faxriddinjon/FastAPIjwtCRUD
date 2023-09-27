from typing import List, Union
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    # user_id: int
    
    class Config():
        orm_mode=True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    # blogs: List
    
    class Config():
        orm_mode=True


class ShowBlog(Blog):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode=True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    email: Union[str, None]=None


class Login(BaseModel):
    username: str
    password: str

