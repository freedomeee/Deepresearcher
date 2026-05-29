# 1. 进入后端目录
cd helloagents-deepresearch/backend

# 2. 安装依赖
# 方式1：使用uv（推荐，更快的Python包管理器）
uv sync

# 方式2：使用pip
pip install -e .

# 3. 配置环境变量
cp .env.example .env

# 4. 编辑.env文件，填入你的API密钥
# 使用你喜欢的编辑器打开.env文件
# 至少需要配置：
# - LLM_PROVIDER（如 openai、deepseek、qwen）
# - LLM_API_KEY（你的LLM API密钥）
# - SEARCH_API（如 duckduckgo、tavily）

# 5. 启动后端
python src/main.py
