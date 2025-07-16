#!/bin/bash

# Render 构建脚本
echo "🚀 开始构建 Gemini Balance 应用..."

# 设置 Python 版本
echo "📋 使用 Python 版本: $(python --version)"

# 升级 pip
echo "⬆️ 升级 pip..."
pip install --upgrade pip

# 安装依赖
echo "📦 安装 Python 依赖..."
pip install -r requirements.txt

# 运行初始化脚本
echo "🔧 运行环境初始化..."
python init_render.py

# 设置权限
echo "🔐 设置文件权限..."
chmod +x app/main.py
chmod +x start.sh

echo "✅ 构建完成！"
