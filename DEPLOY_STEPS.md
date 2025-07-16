# 🚀 Gemini Balance - Render 部署步骤

## 第一步：在 Render 创建服务

1. **登录 Render**
   - 访问 [render.com](https://render.com)
   - 登录您的账户

2. **创建 Web Service**
   - 点击 "New +" → "Web Service"
   - 选择 "Connect a repository"
   - 连接您的 GitHub 账户
   - 选择这个仓库

3. **基本配置**
   ```
   Name: gemini-balance
   Environment: Python 3
   Region: Oregon (US West)
   Branch: main
   ```

4. **构建和启动配置**
   ```
   Build Command: chmod +x build.sh && ./build.sh
   Start Command: python run.py
   ```

## 第二步：设置环境变量

在 Render 的 Environment 标签页中添加：

### 必需变量
```bash
API_KEYS=["your-actual-gemini-api-key"]
ALLOWED_TOKENS=["your-access-token"]
AUTH_TOKEN=your-admin-token
```

### 数据库配置
```bash
DATABASE_TYPE=sqlite
SQLITE_DATABASE=gemini_balance
```

### 模型配置（已包含 gemini-2.5-pro）
```bash
IMAGE_MODELS=["gemini-2.0-flash-exp", "gemini-2.5-pro"]
SEARCH_MODELS=["gemini-2.0-flash-exp", "gemini-2.5-pro"]
THINKING_MODELS=["gemini-2.5-pro"]
```

## 第三步：部署

1. **点击 "Create Web Service"**
2. **等待构建完成**（约 3-5 分钟）
3. **检查部署状态**

## 第四步：验证部署

1. **访问应用 URL**
2. **使用 AUTH_TOKEN 登录**
3. **测试 API 端点**：
   ```bash
   curl https://your-app.onrender.com/health
   ```

## 🎯 gemini-2.5-pro 使用示例

```bash
curl -X POST "https://your-app.onrender.com/v1/chat/completions" \
  -H "Authorization: Bearer your-access-token" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.5-pro",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## 🔧 故障排除

- **构建失败**：检查构建日志
- **启动失败**：验证环境变量格式
- **API 错误**：确认 Gemini API Key 有效

## 📱 管理界面

- 主页：`https://your-app.onrender.com/`
- 配置：`https://your-app.onrender.com/config`
- 监控：`https://your-app.onrender.com/keys`
