#!/usr/bin/env python3
"""
部署验证脚本
用于检查 Render 部署是否成功
"""

import requests
import json
import sys
import time
from urllib.parse import urljoin

def test_health_endpoint(base_url):
    """测试健康检查端点"""
    try:
        url = urljoin(base_url, "/health")
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("✅ 健康检查通过")
            return True
        else:
            print(f"❌ 健康检查失败: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 健康检查异常: {e}")
        return False

def test_models_endpoint(base_url, token):
    """测试模型列表端点"""
    try:
        url = urljoin(base_url, "/v1/models")
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            models = [model["id"] for model in data.get("data", [])]
            
            # 检查是否包含 gemini-2.5-pro
            if "gemini-2.5-pro" in models:
                print("✅ gemini-2.5-pro 模型可用")
            else:
                print("⚠️ gemini-2.5-pro 模型未找到")
            
            # 检查特殊功能模型
            special_models = [
                "gemini-2.5-pro-search",
                "gemini-2.5-pro-image"
            ]
            
            for model in special_models:
                if model in models:
                    print(f"✅ {model} 功能可用")
                else:
                    print(f"⚠️ {model} 功能未启用")
            
            print(f"📋 总共发现 {len(models)} 个模型")
            return True
        else:
            print(f"❌ 模型列表获取失败: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 模型列表测试异常: {e}")
        return False

def test_chat_endpoint(base_url, token):
    """测试聊天端点"""
    try:
        url = urljoin(base_url, "/v1/chat/completions")
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gemini-2.5-pro",
            "messages": [{"role": "user", "content": "Hello! This is a test."}],
            "max_tokens": 50
        }
        
        response = requests.post(url, headers=headers, json=data, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if "choices" in result and len(result["choices"]) > 0:
                print("✅ gemini-2.5-pro 聊天功能正常")
                return True
            else:
                print("❌ 聊天响应格式异常")
                return False
        else:
            print(f"❌ 聊天测试失败: {response.status_code}")
            if response.text:
                print(f"错误信息: {response.text}")
            return False
    except Exception as e:
        print(f"❌ 聊天测试异常: {e}")
        return False

def main():
    """主函数"""
    if len(sys.argv) < 3:
        print("使用方法: python verify_deployment.py <BASE_URL> <ACCESS_TOKEN>")
        print("示例: python verify_deployment.py https://your-app.onrender.com your-token")
        sys.exit(1)
    
    base_url = sys.argv[1].rstrip('/')
    token = sys.argv[2]
    
    print(f"🔍 开始验证部署: {base_url}")
    print("=" * 50)
    
    # 等待服务启动
    print("⏳ 等待服务启动...")
    time.sleep(5)
    
    success_count = 0
    total_tests = 3
    
    # 测试健康检查
    if test_health_endpoint(base_url):
        success_count += 1
    
    # 测试模型列表
    if test_models_endpoint(base_url, token):
        success_count += 1
    
    # 测试聊天功能
    if test_chat_endpoint(base_url, token):
        success_count += 1
    
    print("=" * 50)
    print(f"📊 测试结果: {success_count}/{total_tests} 通过")
    
    if success_count == total_tests:
        print("🎉 部署验证成功！所有功能正常工作")
        print(f"🌐 管理界面: {base_url}/config")
        print(f"📊 监控面板: {base_url}/keys")
    else:
        print("⚠️ 部署验证部分失败，请检查配置和日志")
        sys.exit(1)

if __name__ == "__main__":
    main()
