# 🚀 PromptPilot

> **An intelligent local AI routing engine that automatically selects the best LLM for every prompt.**

PromptPilot is an OpenAI-compatible API server that intelligently routes user prompts to the most suitable local language model running on **Ollama**. It seamlessly integrates with **Open WebUI**, supports multimodal (vision) models, and is designed with future machine learning-based routing in mind.

---

## ✨ Features

- 🧠 Intelligent AI model routing
- ⚡ OpenAI-compatible API
- 💻 Open WebUI integration
- 👀 Vision model support
- 🖼️ Base64 image support
- 🎯 Manual model selection
- 📝 Request logging
- 🔌 Ollama backend
- 🛠️ Lightweight and easy to extend

---

# 📦 Supported Models

| Model | Purpose |
|--------|---------|
| Qwen Coder | Programming, debugging, algorithms, software engineering |
| DeepSeek | Complex reasoning, mathematics, logic, planning |
| Hermes | Creative writing, emails, roleplay, content generation |
| Gemma | General conversation and lightweight routing |
| Qwen VL | Image understanding and multimodal tasks |

Adding new models is simple and only requires minimal configuration.

---

# 🏗️ Architecture

```
                    User
                      │
                      ▼
              Open WebUI / API Client
                      │
                      ▼
                PromptPilot API
                      │
          ┌───────────┴───────────┐
          │                       │
      AI Router             Vision Detection
          │                       │
          └───────────┬───────────┘
                      ▼
               Selected Ollama Model
                      │
                      ▼
                  Final Response
```

---

# ⚙️ How Routing Works

PromptPilot analyzes the user's prompt and automatically selects the most suitable model.

Examples:

| Prompt | Selected Model |
|---------|----------------|
| Reverse a linked list in Python | Qwen |
| Solve this calculus proof | DeepSeek |
| Write a horror story | Hermes |
| Explain what a CPU is | Gemma |
| Describe this uploaded image | Vision |

Manual overrides are also supported:

```
@qwen
@deepseek
@hermes
@gemma
@vision
```

---

# 👀 Vision Support

PromptPilot automatically routes image requests to a vision-capable model.

Supported:

- Image description
- OCR
- Screenshot analysis
- Charts
- Diagrams
- Image question answering

Images uploaded from Open WebUI are automatically converted to the format expected by Ollama.

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/PromptPilot.git
cd PromptPilot
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start Ollama

```bash
ollama serve
```

Run PromptPilot

```bash
python main.py
```

Connect Open WebUI to

```
http://localhost:8000/v1
```

---

# 📸 Screenshots

> *(Add screenshots of PromptPilot + Open WebUI here)*

---

# 🛣️ Roadmap

## ✅ v0.7.0

- OpenAI Compatible API
- Automatic Model Routing
- Open WebUI Integration
- Vision Support
- Manual Model Overrides
- Logging System
- Base64 Image Support
- Improved Router Prompt

---

## 🚧 v1.0.0

- Stateless conversation handling
- Better OpenAI compatibility
- Multiple image support
- Improved routing accuracy
- Better logging
- Production-ready architecture
- Comprehensive testing

---

# 🔬 Future Development

PromptPilot is designed to evolve into an intelligent AI routing platform rather than relying solely on prompt engineering.

## 🧠 Zero-Shot Intent Classification

Future versions will replace prompt-based routing with lightweight machine learning classifiers capable of understanding user intent without predefined keywords.

Potential models include:

- ModernBERT
- BGE Reranker
- Nomic Embed
- Lightweight Transformer Classifiers

---

## 📊 Confidence-Based Hybrid Routing

Future routing will combine machine learning with LLM reasoning.

```
User Prompt
      │
      ▼
Zero-Shot Classifier
      │
      ├── Confidence ≥ 90%
      │
      │      Route Directly
      │
      └── Confidence < 90%
               │
               ▼
          Gemma Router
               │
               ▼
        Final Model Selection
```

This hybrid architecture improves both speed and routing accuracy.

---

## 🤖 Trainable Routing Model

PromptPilot will eventually support a dedicated routing model trained on real routing data.

```
Prompt
   │
   ▼
Embedding Model
   │
   ▼
ML Classifier
   │
   ▼
Predicted Model
```

This enables routing decisions without relying on handcrafted prompts.

---

## 📈 Continuous Learning

Future releases may optionally learn from user feedback.

Example:

```
Prompt
   │
   ▼
Qwen Selected
   │
User switches to DeepSeek
   │
   ▼
Store Correction
   │
   ▼
Improve Future Predictions
```

This creates a continuously improving routing system.

---

## ⚡ Multi-Stage Routing

Future versions may combine multiple routing strategies.

```
Prompt
   │
   ▼
Keyword Detection
   │
   ▼
Zero-Shot Classifier
   │
   ▼
Confidence Check
   │
   ├── High Confidence
   │       │
   │       ▼
   │   Route Request
   │
   └── Low Confidence
           │
           ▼
      Gemma Router
           │
           ▼
      Final Selection
```

---

## 🌍 Planned Integrations

- LM Studio
- llama.cpp
- vLLM
- OpenRouter
- MCP
- Tool Calling
- Local Embedding Models
- RAG Pipelines

---

# 🤝 Contributing

Contributions, feature requests, and bug reports are welcome.

If you have ideas for improving routing accuracy, new model integrations, or architecture improvements, feel free to open an issue or submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Acknowledgements

Built using:

- Ollama
- Open WebUI
- FastAPI
- Python

Special thanks to the open-source AI community for making local LLMs more accessible.

---

## 🚀 PromptPilot v0.7.0

The journey has just begun.

The long-term goal is to build a fast, intelligent, modular AI routing platform that automatically selects the best model for every task using modern machine learning techniques.

If you find this project useful, consider giving it a ⭐ on GitHub!