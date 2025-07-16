#!/usr/bin/env python3
"""
Render 环境初始化脚本
确保必要的目录和文件存在
"""

import os
import sys
from pathlib import Path

def create_directories():
    """创建必要的目录"""
    directories = [
        "data",
        "logs",
        "app/static",
        "app/templates"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ 创建目录: {directory}")

def check_environment():
    """检查环境变量"""
    required_env_vars = [
        "API_KEYS",
        "ALLOWED_TOKENS"
    ]
    
    missing_vars = []
    for var in required_env_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"❌ 缺少必要的环境变量: {', '.join(missing_vars)}")
        print("请在 Render 控制台中设置这些环境变量")
        return False
    
    print("✓ 环境变量检查通过")
    return True

def main():
    """主函数"""
    print("🚀 初始化 Render 环境...")
    
    # 创建目录
    create_directories()
    
    # 检查环境变量
    if not check_environment():
        sys.exit(1)
    
    print("✅ Render 环境初始化完成!")

if __name__ == "__main__":
    main()
