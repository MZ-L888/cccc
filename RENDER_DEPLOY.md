# Gemini Balance - Render 部署指南

本指南将帮助您在 Render 平台上轻松部署 Gemini Balance 应用，并添加 gemini-2.5-pro 模型支持。

## 🚀 快速部署

### 方法一：使用 GitHub 仓库部署（推荐）

1. **Fork 或克隆仓库**
   - Fork 这个仓库到您的 GitHub 账户
   - 或者将代码推送到您的 GitHub 仓库

2. **在 Render 创建 Web Service**
   - 登录 [Render](https://render.com)
   - 点击 "New +" → "Web Service"
   - 连接您的 GitHub 仓库
   - 选择包含 Gemini Balance 代码的仓库

3. **配置部署设置**
   ```
   Name: gemini-balance
   Environment: Python 3
   Build Command: chmod +x build.sh && ./build.sh
   Start Command: python run.py
   ```

### 方法二：使用 render.yaml 自动部署

1. **确保仓库包含 render.yaml 文件**
   - 本项目已包含 `render.yaml` 配置文件
   - 该文件包含所有必要的部署配置

2. **在 Render 导入配置**
   - 在 Render Dashboard 中选择 "New +" → "Blueprint"
   - 连接您的 GitHub 仓库
   - Render 会自动读取 `render.yaml` 配置

## ⚙️ 环境变量配置

在 Render 的 Environment 标签页中设置以下环境变量：

### 必需配置
```bash
# API Keys（必填）
API_KEYS=["your-gemini-api-key-1", "your-gemini-api-key-2"]
ALLOWED_TOKENS=["your-access-token-1", "your-access-token-2"]
AUTH_TOKEN=your-super-admin-token

# 数据库配置（Render 免费版推荐 SQLite）
DATABASE_TYPE=sqlite
SQLITE_DATABASE=./data/gemini_balance.db
```

### 模型配置（包含 gemini-2.5-pro）
```bash
# 支持的模型列表
IMAGE_MODELS=["gemini-2.0-flash-exp", "gemini-2.5-pro"]
SEARCH_MODELS=["gemini-2.0-flash-exp", "gemini-2.5-pro"]
THINKING_MODELS=["gemini-2.5-pro"]
THINKING_BUDGET_MAP={"gemini-2.5-pro": 1000.0}

# 基础配置
BASE_URL=https://generativelanguage.googleapis.com/v1beta
TEST_MODEL=gemini-1.5-flash
```

### 可选配置
```bash
# 功能开关
TOOLS_CODE_EXECUTION_ENABLED=false
SHOW_SEARCH_LINK=true
SHOW_THINKING_PROCESS=true
URL_NORMALIZATION_ENABLED=false

# 系统配置
MAX_FAILURES=3
MAX_RETRIES=3
TIME_OUT=300
LOG_LEVEL=INFO
TIMEZONE=Asia/Shanghai

# 图像生成（需要付费 API Key）
CREATE_IMAGE_MODEL=imagen-3.0-generate-002
PAID_KEY=your-paid-api-key
UPLOAD_PROVIDER=smms
```

## 📋 部署步骤详解

### 1. 准备工作
- 确保您有有效的 Gemini API Key
- 注册 Render 账户（免费版即可）
- 准备 GitHub 仓库

### 2. 配置仓库
确保您的仓库包含以下文件：
- `build.sh` - 构建脚本
- `render.yaml` - Render 配置文件
- `Procfile` - 备用启动配置
- `init_render.py` - 环境初始化脚本
- `.env.render.example` - 环境变量示例

### 3. 部署到 Render
1. 在 Render 创建新的 Web Service
2. 连接 GitHub 仓库
3. 设置环境变量
4. 点击 "Create Web Service"

### 4. 验证部署
- 等待构建完成（通常 2-5 分钟）
- 访问提供的 URL
- 使用配置的 AUTH_TOKEN 登录管理界面

## 🔧 故障排除

### 常见问题

1. **构建失败：找不到 build.sh**
   - 确保 `build.sh` 文件存在且有执行权限
   - 检查文件编码是否为 UTF-8

2. **应用启动失败**
   - 检查环境变量是否正确设置
   - 确保 API_KEYS 和 ALLOWED_TOKENS 格式正确（JSON 数组）

3. **数据库连接错误**
   - 使用 SQLite：确保 `DATABASE_TYPE=sqlite`
   - 检查数据目录权限

4. **API 调用失败**
   - 验证 Gemini API Key 是否有效
   - 检查网络连接和代理设置

### 日志查看
在 Render Dashboard 的 "Logs" 标签页查看详细日志信息。

## 🎯 gemini-2.5-pro 模型使用

部署成功后，您可以使用以下方式调用 gemini-2.5-pro 模型：

### OpenAI 格式 API
```bash
curl -X POST "https://your-app.onrender.com/v1/chat/completions" \
  -H "Authorization: Bearer your-access-token" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.5-pro",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

### 特殊功能
- **搜索功能**: 使用 `gemini-2.5-pro-search`
- **图像功能**: 使用 `gemini-2.5-pro-image`
- **思维过程**: 使用 `gemini-2.5-pro`（自动启用思维过程）

## 📚 更多资源

- [Render 官方文档](https://render.com/docs)
- [Gemini API 文档](https://ai.google.dev/docs)
- [项目 GitHub 仓库](https://github.com/snailyp/gemini-balance)

## 🔗 一键部署链接

点击下面的按钮可以直接在 Render 上部署：

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/your-username/gemini-balance)

> 注意：请将 URL 中的 `your-username` 替换为您的 GitHub 用户名

## 💡 提示

- Render 免费版有一定限制，建议用于测试和小规模使用
- 生产环境建议升级到付费计划
- 定期备份重要数据和配置
- 首次部署可能需要 5-10 分钟
- 应用会在 15 分钟无活动后休眠（免费版）
