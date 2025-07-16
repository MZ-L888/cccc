#!/bin/bash

# Render 启动脚本
echo "启动 Gemini Balance 应用..."

# 设置环境变量
export PORT=${PORT:-8000}

# 确保数据目录存在
mkdir -p data
mkdir -p logs

# 启动应用
echo "在端口 $PORT 上启动应用..."
exec uvicorn app.main:app --host 0.0.0.0 --port $PORT --no-access-log
