from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from .config import settings

# 异步引擎配置
engine = create_async_engine(
    settings.DATABASE_URL,  # 从配置读取数据库连接字符串
    echo=False,              # 是否开启SQL语句日志输出
    future=True             # 启用 SQLAlchemy 2.0 兼容模式
)

# 创建异步会话工厂
async_session = sessionmaker(
    bind=engine,            # 绑定异步引擎
    class_=AsyncSession,    # 指定生成异步会话类
    expire_on_commit=False  # 提交后不自动过期对象
)

# 数据库会话依赖注入
async def get_db() -> AsyncSession:
    async with async_session() as session:  # 创建异步会话上下文
        yield session                        # 生成可重用的会话实例

# 应用生命周期管理
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 应用启动时创建所有数据库表
    async with engine.begin() as conn:       # 获取异步连接
        await conn.run_sync(SQLModel.metadata.create_all)  # 同步执行建表
    yield
    # 应用关闭时释放数据库连接
    await engine.dispose()