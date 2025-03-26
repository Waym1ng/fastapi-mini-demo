
class Settings:
    # DATABASE_URL: str = "sqlite+aiosqlite:///./database.db"
    DATABASE_URL: str = "mysql+asyncmy://mingming:root@127.0.0.1:3306/t-fastapi-db"

settings = Settings()