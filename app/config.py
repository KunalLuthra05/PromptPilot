# ===========================
# PromptPilot Model Config
# ===========================

QWEN = "qwen2.5-coder:7b"
DEEPSEEK = "deepseek-r1:7b"
HERMES = "hermes3:8b"
GEMMA = "gemma3:4b"
VISION = "qwen2.5vl:7b"

# Small routing model
ROUTER = "qwen2.5:3b"

AVAILABLE_MODELS = [
    QWEN,
    DEEPSEEK,
    HERMES,
    GEMMA,
    VISION
]

DEFAULT_MODEL = GEMMA