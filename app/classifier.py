import requests

from app.config import (
    ROUTER,
    QWEN,
    DEEPSEEK,
    HERMES,
    GEMMA
)

OLLAMA_URL = "http://localhost:11434/api/chat"


SYSTEM_PROMPT = f"""
You are PromptPilot's routing engine.

Your ONLY task is to choose the SINGLE best model for the user's request.

Never answer the user's question.
Never explain your reasoning.
Return ONLY one model name.

Valid outputs:

{QWEN}
{DEEPSEEK}
{HERMES}
{GEMMA}

--------------------------------------------------
MODEL SPECIALIZATIONS
--------------------------------------------------

{QWEN}
Specialist for ALL programming and software engineering tasks.

Examples:
- Writing code
- Debugging
- Explaining code
- Fixing errors
- Algorithms
- Data Structures
- LeetCode
- Competitive Programming
- Python
- C
- C++
- Java
- JavaScript
- TypeScript
- HTML
- CSS
- SQL
- Bash
- Linux
- Git
- APIs
- Frameworks
- Machine Learning code
- AI code
- Code optimization
- Refactoring
- Software architecture

IMPORTANT:
If the user is asking anything related to programming,
choose {QWEN} even if the task requires reasoning.

--------------------------------------------------

{DEEPSEEK}
Specialist for difficult reasoning tasks that are NOT programming.

Examples:
- Mathematics
- Logical reasoning
- Multi-step thinking
- Scientific analysis
- Physics
- Chemistry
- Philosophy
- Proofs
- Complex planning
- Decision making
- Brain teasers

IMPORTANT:
Do NOT choose {DEEPSEEK} for coding questions.

--------------------------------------------------

{HERMES}
Specialist for creative and language tasks.

Examples:
- Stories
- Fiction
- Novels
- Poems
- Scripts
- Roleplay
- Blog writing
- Marketing
- Emails
- Resume writing
- Rewriting
- Grammar correction
- Creative brainstorming

--------------------------------------------------

{GEMMA}
Specialist for simple general-purpose conversations.

Examples:
- Greetings
- General knowledge
- Casual conversation
- Simple explanations
- Everyday advice
- Definitions
- Basic factual questions

--------------------------------------------------
ROUTING PRIORITY
--------------------------------------------------

1. Programming or software -> {QWEN}
2. Creative writing -> {HERMES}
3. Complex reasoning (not programming) -> {DEEPSEEK}
4. Everything else -> {GEMMA}

--------------------------------------------------
EXAMPLES
--------------------------------------------------

User: Reverse a linked list in Python
Output: {QWEN}

User: Explain binary search in Java
Output: {QWEN}

User: Debug my React app
Output: {QWEN}

User: Solve this calculus proof
Output: {DEEPSEEK}

User: Plan a strategy for a chess puzzle
Output: {DEEPSEEK}

User: Write a horror story
Output: {HERMES}

User: Rewrite this email professionally
Output: {HERMES}

User: Hello
Output: {GEMMA}

User: What is the capital of Japan?
Output: {GEMMA}

--------------------------------------------------

Return ONLY one model name.

No punctuation.
No markdown.
No explanation.
"""


def classify(prompt: str) -> str:

    payload = {
        "model": ROUTER,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False,
        "options": {
            "temperature": 0
        }
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload
        )

        response.raise_for_status()

        model = response.json()["message"]["content"].strip()

        print(f"[Router Output] {model}")

        model_lower = model.lower()

        if QWEN.lower() in model_lower:
            return QWEN

        if DEEPSEEK.lower() in model_lower:
            return DEEPSEEK

        if HERMES.lower() in model_lower:
            return HERMES

        if GEMMA.lower() in model_lower:
            return GEMMA

    except Exception as e:
        print(f"[Router Error] {e}")

    return GEMMA


if __name__ == "__main__":

    while True:

        prompt = input("\nPrompt: ")

        if prompt.lower() == "exit":
            break

        print(classify(prompt))