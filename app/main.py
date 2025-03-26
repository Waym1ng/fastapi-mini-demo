from fastapi import FastAPI
from app.core.database import lifespan
from app.routers import users

app = FastAPI(
    title="FastAPI Starter",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# 集成路由
app.include_router(users.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=False)