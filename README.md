# Sample Agent Development Kit (ADK)

This project demonstrates how to build an AI-powered agents using **Agent Development Kit (ADK)** and **Gemini APIs** as well as other LLM APIs.

---

## 🚀 Features

- Modular multi-agent architecture
- LLM-powered agenta
- Visual content enhancement
- Auto-formatting with narration, colors, and transitions
- Optional looping agent for refinement
- Built with Google ADK, Gemini API and DeepSeek API

---

## 🤖 Architecture Overview

```
Parent Agent (LLM Chatbot)
│
├── 📝 Script Writer Agent
│   └─ Uses Gemini API to fetch & generate content
│
├── 👁️ Visualizer Agent
│   └─ Enhances script with visual cues and layout instructions
│
├── 🎨 Formatter Agent
│   └─ Formats the final output with narration, styles, timing
│
└── 🔁 (Optional) LoopAgent
    └─ Repeats the workflow for improved results
```

---

## 🧠 Agent Config Example (YAML)

```yaml
name: script_writer_agent
model: gemini-1.5-flash
instruction: generate_script_steps.yaml
description: Collects topic-related data and drafts a video script.
output_key: script_draft_output
```

### Instruction File Example

```yaml
steps:
  - Search Google using Gemini API for topic keyword
  - Collect 5–7 unique content pieces
  - Remove duplicates and unrelated data
  - Save result to output key
```

---



## 🛠️ Tech Stack

- **Google ADK** – Agent framework
- **Gemini API** – LLM for content generation
- **Instruction Files (YAML)** – Agent guidance
- **Session & Memory** – Persistent agent communication

---

## 📦 Setup

> ⚠️ This is a conceptual/experimental project. Setup instructions below are generalized.

1. **Clone the Repo**
   ```bash
   git clone https://github.com/kuahoong/adk.git
   ```

2. **Install Dependencies**
   Make sure Python and required SDKs are installed.
   ```bash
   pip install google-adk
   ```

3. **Configure Agents**
   you can view the agent file if any changes needed.

4. **Run the Parent Agent**
   ```bash
   adk web
   ```

---

## 📈 Use Cases

- Automated content pipelines
- Marketing video scripting
- Explainers and educational video drafts
- Creative prototyping with AI

---

## 📚 Related Reading

- [Google Cloud Blog: Introducing ADK](https://cloud.google.com/blog/)
- [Gemini API Overview](https://ai.google.dev/)
