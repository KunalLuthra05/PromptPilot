# Model Names

QWEN = "qwen2.5-coder:7b"
DEEPSEEK = "deepseek-r1:7b"
HERMES = "hermes3:8b"
GEMMA = "gemma3:4b"
VISION = "qwen2.5vl:7b"


# Category -> Model Mapping

MODEL_MAP = {
    "CODING": QWEN,
    "REASONING": DEEPSEEK,
    "WRITING": HERMES,
    "GENERAL": GEMMA,
    "VISION": VISION
}


# Keyword Lists

CODING_KEYWORDS = [
    "python",
    "java",
    "c++",
    "javascript",
    "html",
    "css",
    "sql",
    "bug",
    "error",
    "react",
    "django",
    "flask",
    "api"
]

REASONING_KEYWORDS = [
    "dsa",
    "algorithm",
    "graph",
    "tree",
    "complexity",
    "dynamic programming",
    "linked list"
]

WRITING_KEYWORDS = [
    "email",
    "essay",
    "letter",
    "resume",
    "blog"
]