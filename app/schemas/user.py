from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    age: int | None = None

class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    age: int | None = None
    is_active: bool | None = None