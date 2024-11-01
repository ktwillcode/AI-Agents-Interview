# LLM Interview Simulator 🤖

A fascinating experiment to evaluate how different Large Language Models (LLMs) perform in simulated job interviews. This project creates a controlled environment where multiple LLM models play the role of job candidates while being interviewed by a consistent interviewer model.

![LLM Interview Simulator Demo](demo/interview-simulator-demo.png)
*Interactive interview simulation showing real-time conversation between AI interviewer and candidate*

## 📋 Table of Contents
- [Process Flow](#-process-flow)
- [Project Overview](#-project-overview)
- [Models Used](#-models-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Sample Output](#-sample-output)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)


## 🔄 Process Flow

### 1. System Setup Flow
```mermaid
flowchart LR
    A[Start] -->|Initialize| B[System Setup]
    B --> C[Load Models]
    B --> D[Configure Job Roles]
    C --> E[Setup Interviewer]
    C --> F[Setup Candidates]
    
    style A fill:#4CAF50,color:white
    style B fill:#2196F3,color:white
    style C fill:#9C27B0,color:white
    style D fill:#FF9800,color:white
    style E fill:#E91E63,color:white
    style F fill:#673AB7,color:white
```

### 2. Interview Process Flow
```mermaid
flowchart LR
    A[Start Interview] -->|Generate| B[Questions]
    B -->|Collect| C[Responses]
    C -->|Analyze| D[Feedback]
    D -->|Next Question| B
    D -->|Complete| E[Evaluation]
    
    style A fill:#4CAF50,color:white
    style B fill:#2196F3,color:white
    style C fill:#9C27B0,color:white
    style D fill:#FF9800,color:white
    style E fill:#E91E63,color:white
```

### 3. Evaluation Flow
```mermaid
flowchart LR
    A[Evaluation] -->|Generate| B[Scores]
    B -->|Identify| C[Strengths]
    B -->|Identify| D[Weaknesses]
    C --> E[Final Report]
    D --> E
    
    style A fill:#4CAF50,color:white
    style B fill:#2196F3,color:white
    style C fill:#9C27B0,color:white
    style D fill:#FF9800,color:white
    style E fill:#E91E63,color:white
```

## 🎯 Project Overview

This project simulates job interviews using different LLM models as candidates, while maintaining a consistent interviewer (Co-founder/CEO) model. The simulation:

- 📝 Conducts structured interviews for various job positions
- 🤖 Uses different LLM models to simulate candidate responses
- 📊 Provides comprehensive evaluation and feedback
- 📈 Generates comparative analysis across different models
- 💡 Offers practical interview improvement suggestions

## 🤖 Models Used

### Interviewer
```python
Model: groq/llama-3.1-8b-instant
Role: Co-founder and CEO
Purpose: Consistent evaluation across all interviews
```

### Candidates
| Model | Type | Purpose |
|-------|------|---------|
| groq/llama-3.1-8b-instant | Base Model | Quick responses |
| groq/llama3-8b-8192 | Enhanced | Detailed analysis |
| groq/mixtral-8x7b-32768 | Advanced | Complex reasoning |
| groq/llama2-70b-4096 | Large-scale | Comprehensive responses |

## 🔧 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/llm-interview-simulator.git
cd llm-interview-simulator
```

2. **Create and activate virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
```bash
echo "GROQ_API_KEY=your_api_key_here" > .env
```

## 💻 Usage

1. **Run the simulation:**
```bash
python main.py
```

2. **Choose a job title:**
```python
job_titles = [
    "Marketing Associate",
    "Business Development Representative",
    "Product Manager",
    "Customer Success Representative",
    "Data Analyst",
    "AI Engineer"
]
```

## 📊 Features

### Interview Process
- 🔄 Dynamic question generation
- 💬 Natural conversation flow
- 🎯 Technical skill assessment
- 🤝 Cultural fit evaluation

### Evaluation Metrics
| Metric | Description |
|--------|-------------|
| Decision | Pass/Fail outcome |
| Score | 0-100 numerical rating |
| Strengths | Key positive attributes |
| Improvements | Areas for development |
| Tips | Interview improvement suggestions |
| Reasoning | Detailed evaluation logic |

## 📁 Project Structure

```
llm-interview-simulator/
├── 📄 agents.py           # Agent definitions
├── 📄 tasks.py           # Interview tasks
├── 📄 interview_simulation.py  # Core logic
├── 📄 main.py           # Entry point
├── 📄 requirements.txt  # Dependencies
└── 📄 README.md        # Documentation
```

## 🔍 Sample Output

![Sample Evaluation](demo/sample-evaluation.png)
*Sample evaluation dashboard showing comparative analysis*

### Output Format
```json
{
    "job_title": "AI Engineer",
    "interview_date": "2024-03-31 14:30:22",
    "candidates": {
        "candidate1": {
            "model": "groq/llama-3.1-8b-instant",
            "score": 85,
            "evaluation": "..."
        }
    },
    "comparative_analysis": "..."
}
```

## 🤝 Contributing

We welcome contributions! Areas for improvement:
- 📝 New job positions
- 🤖 Additional LLM models
- 📊 Enhanced metrics
- 💡 Feature additions

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- 🛠️ Built with CrewAI framework
- 🤖 Powered by Groq's LLM models
- 💼 Inspired by real-world interviews

## ⚠️ Disclaimer

This is an experimental project for research and educational purposes. The simulations should not be used as the sole basis for actual hiring decisions.

## 📊 Results Dashboard

![Results Dashboard](demo/results-dashboard.png)
*Interactive dashboard showing model performance comparison*

Key metrics displayed:
- ⭐ Response quality scores
- 🤝 Cultural fit assessment
- 🧠 Technical knowledge evaluation
- 💬 Communication style analysis

---
Made with ❤️ by [Your Name]
