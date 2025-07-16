# Gemini Balance - Render 一键部署版

🚀 **支持 gemini-2.5-pro 模型的 Gemini API 代理服务**

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

## ✨ 特性

- 🔄 **多 API Key 负载均衡**
- 🤖 **支持 gemini-2.5-pro 最新模型**
- 🔍 **集成搜索功能**
- 🎨 **图像生成和处理**
- 🧠 **思维过程展示**
- 🌐 **OpenAI 格式兼容**
- 📊 **实时监控面板**

## 🚀 快速部署

### 1. 点击部署按钮
点击上方的 "Deploy to Render" 按钮

### 2. 设置环境变量
在 Render 控制台中设置以下必需变量：

```bash
API_KEYS=["your-gemini-api-key"]
ALLOWED_TOKENS=["your-access-token"]
AUTH_TOKEN=your-admin-token
```

### 3. 等待部署完成
通常需要 3-5 分钟

### 4. 访问应用
使用提供的 URL 访问您的 Gemini Balance 服务

## 🎯 gemini-2.5-pro 使用示例

### 基础对话
```bash
curl -X POST "https://your-app.onrender.com/v1/chat/completions" \
  -H "Authorization: Bearer your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.5-pro",
    "messages": [{"role": "user", "content": "你好！"}]
  }'
```

### 搜索功能
```bash
curl -X POST "https://your-app.onrender.com/v1/chat/completions" \
  -H "Authorization: Bearer your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.5-pro-search",
    "messages": [{"role": "user", "content": "最新的AI发展趋势"}]
  }'
```

### 图像处理
```bash
curl -X POST "https://your-app.onrender.com/v1/chat/completions" \
  -H "Authorization: Bearer your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.5-pro-image",
    "messages": [{"role": "user", "content": "描述这张图片", "image_url": "https://example.com/image.jpg"}]
  }'
```

## 📋 环境变量说明

| 变量名 | 必需 | 说明 | 示例 |
|--------|------|------|------|
| `API_KEYS` | ✅ | Gemini API 密钥列表 | `["key1", "key2"]` |
| `ALLOWED_TOKENS` | ✅ | 允许访问的令牌 | `["token1", "token2"]` |
| `AUTH_TOKEN` | ✅ | 管理员令牌 | `admin-token-123` |
| `DATABASE_TYPE` | ❌ | 数据库类型 | `sqlite` (默认) |
| `IMAGE_MODELS` | ❌ | 支持图像的模型 | `["gemini-2.5-pro"]` |
| `SEARCH_MODELS` | ❌ | 支持搜索的模型 | `["gemini-2.5-pro"]` |

## 🔧 管理界面

部署成功后，访问以下路径：

- **主页**: `https://your-app.onrender.com/`
- **配置管理**: `https://your-app.onrender.com/config`
- **密钥状态**: `https://your-app.onrender.com/keys`
- **日志查看**: `https://your-app.onrender.com/logs`
- **健康检查**: `https://your-app.onrender.com/health`

## 📚 API 端点

### OpenAI 兼容格式
- `GET /v1/models` - 获取模型列表
- `POST /v1/chat/completions` - 聊天完成
- `POST /v1/embeddings` - 文本嵌入
- `POST /v1/images/generations` - 图像生成

### Gemini 原生格式
- `GET /v1beta/models` - 获取模型列表
- `POST /v1beta/models/{model}:generateContent` - 生成内容
- `POST /v1beta/models/{model}:streamGenerateContent` - 流式生成

## 🆘 故障排除

### 常见问题

1. **部署失败**
   - 检查 GitHub 仓库是否包含所有必需文件
   - 确保 `build.sh` 有执行权限

2. **API 调用失败**
   - 验证 API Key 是否有效
   - 检查令牌格式是否正确

3. **应用无法访问**
   - 等待部署完全完成
   - 检查 Render 服务状态

### 获取帮助

- 查看 [详细部署指南](RENDER_DEPLOY.md)
- 检查 Render 控制台日志
- 访问项目 [GitHub Issues](https://github.com/snailyp/gemini-balance/issues)

## 📄 许可证

本项目采用 CC BY-NC 4.0 许可证，禁止商业用途。

---

⭐ 如果这个项目对您有帮助，请给个 Star！
