# 🧠 AI Local Task Planner

A fully local AI-powered task planning application built using Python, Streamlit, and Ollama.

This project demonstrates:
- Local LLM integration
- Clean Python project architecture
- Virtual environment management
- Git version control workflow

---

## 🚀 Features

- Task prioritization
- Time-block suggestions
- Productivity advice
- Fully offline AI processing (no API calls)
## ✨ New in v1.1.0

- Session-based plan history
- Streaming AI responses
- Streaming Preserved
- Model selector preserved
- Stop generation control
- Dark mode toggle
- Structured planner UI (non-chat format)

---

## 🏗 Architecture

User Interface (Streamlit)
        ↓
Business Logic (planner.py)
        ↓
AI Engine (ai_engine.py)
        ↓
Local LLM via Ollama (LLaMA 3 / Phi3)

---

## 🛠 Tech Stack

- Python
- Streamlit
- Ollama
- LLaMA 3 / Phi3 model
- Virtual Environment (venv)
- Git

---

## ⚡ Setup Instructions

### 1️⃣ Clone Repository

git clone https://github.com/yourusername/AI-Task-Planner-Assistant.git  
cd AI-Task-Planner-Assistant 

### 2️⃣ Create Virtual Environment

python -m venv venv  

### 3️⃣ Activate Environment

Windows:
venv\Scripts\activate  

### 4️⃣ Install Dependencies

pip install -r requirements.txt  

### 5️⃣ Run Application

python -m streamlit run app.py  

---

## 📈 Future Improvements

- Add persistent task storage (SQLite)
- Add streaming responses
- Improve model validation logic
- Add performance benchmarking
- Deploy to cloud

---

## 📚 Learning Goals

This project was built as part of a structured AI engineering learning path.