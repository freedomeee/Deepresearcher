# Deepresearcher

一个本地化的研究与总结助手，基于 `FastAPI`、`HelloAgents` 和 `Vue 3` 构建。它支持通过网页搜索接口进行深度调研，并将结果整理为结构化报告和待办事项。

> 本仓库适合用于本地部署研究型 AI 助手，前端使用 Vite + Vue，后端使用 FastAPI 提供 HTTP 与流式接口。

## 主要功能

- 本地或自定义 LLM 支持（Ollama、LMStudio、兼容 OpenAI API）
- 多搜索后端：DuckDuckGo、Tavily、Perplexity、SearxNG
- 流式研究结果输出（Server-Sent Events）
- 自动生成 Markdown 报告与任务列表
- 支持笔记存储和任务进度追踪

## 目录结构

- `backend/` - 后端服务目录
  - `src/` - FastAPI 应用与 Agent 实现
  - `pyproject.toml` - Python 包与依赖配置
  - `.env.example` - 环境变量示例
- `frontend/` - 前端 Vue 应用
- `.gitignore` - Git 忽略规则

## 环境准备

推荐先在根目录创建 Python 虚拟环境并安装后端依赖：

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
```

前端依赖安装：

```powershell
cd frontend
npm install
```

## 配置后端

复制环境示例并修改配置：

```powershell
cd backend
copy .env.example .env
```

然后根据实际情况修改 `.env`：

- `SEARCH_API`：选择 `duckduckgo`、`tavily`、`perplexity`、`searxng` 或 `advanced`
- `LLM_PROVIDER`：`ollama` / `lmstudio` / `custom`
- `LLM_MODEL_ID`：本地模型名称或自定义模型 ID
- `LLM_API_KEY`：如果使用自定义 OpenAI 兼容服务，填入 API Key
- `LLM_BASE_URL`：自定义 OpenAI 兼容服务地址
- `TAVILY_API_KEY`：Tavily 搜索 API Key

> 注意：不要将真实的 API Key 提交到 GitHub，建议将 `.env` 加入 `.gitignore`。

## 运行后端

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

后端默认监听： `http://localhost:8000`

### 可用接口

- `GET /healthz` - 健康检查
- `POST /research` - 生成研究报告
- `POST /research/stream` - 流式研究结果

## 运行前端

```powershell
cd frontend
npm run dev
```

前端默认启动在： `http://localhost:5173`

## 开发与调试

如果想修改后端逻辑或 Agent 行为，可参考：

- `backend/src/main.py`
- `backend/src/agent.py`
- `backend/src/config.py`
- `backend/src/prompts.py`

如果想修改前端交互，可参考：

- `frontend/src/App.vue`
- `frontend/src/services/api.ts`

## 常见问题

- `gh auth login` 无法访问 GitHub：请检查网络或使用 VPN
- 如果模型连接失败：确认 `LLM_PROVIDER` 和 `*_BASE_URL` 是否正确
- 若需要流式输出，请使用前端或直接调用 `/research/stream` 接口

## 贡献

欢迎继续完善本仓库：

- 增加更多搜索后端支持
- 优化前端交互体验
- 支持更丰富的模型配置与工具调用
- 添加单元测试与 CI

---

如果你希望，我也可以继续帮你把这个 `README` 翻译成英文，或者补充具体运行示例和环境变量说明。