# FastAPI 迷你演示项目

轻量级API服务示例，基于FastAPI框架构建，适合快速上手和开发参考。

## 🚀 主要功能
- ✅ 基础数据CRUD操作
- ✅ 请求参数自动验证
- ✅ 标准化错误响应处理
- ✅ 实时API文档生成（Swagger/Redoc）
- ✅ 连接Mysql数据库

## ⚙️ 技术栈
- Python 3.9+
- FastAPI 0.95+
- Uvicorn 0.22+
- Pydantic 1.10+

## 🛠️ 快速启动
```bash
# 安装依赖
pip install -r requirements.txt

# 启动开发服务器
uvicorn main:app --reload