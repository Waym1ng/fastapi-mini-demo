from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    email: str = Field(max_length=100)
    age: int | None = None
    is_active: bool = Field(default=True)