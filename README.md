# 📊 Stock-Insight — Multi-Agent LLM Stock Analysis System

Stock-Insight is a multi-agent financial analysis system powered by **Google ADK**.
It behaves like a small research team: one agent collects data, others analyze fundamentals,
risks, and valuation, and a final writer produces a clean, structured stock report.

## 🚀 Features

- **Price Lookup** – Real-time stock prices via Yahoo Finance  
- **Automated Data Collection** – Financial metrics + valuation ratios + latest news  
- **Fundamental Analysis** – Revenue, margins, cash flow overview  
- **Risk Analysis** – Extract risks from recent headlines  
- **Valuation Analysis** – Interpret PE, PS, Forward PE  
- **Final Report Writer** – Generates a polished Markdown analysis  
- **Planner Agent** – Orchestrates a 5-step workflow:
  ```
  data → fundamental → risk → valuation → final_writer
  ```

## 🧠 Architecture

```
stock_insight/
│
├── root_agent.py
├── tools/
│   └── financial_tools.py
│
└── sub_agents/
    ├── planner/
    │   └── agent.py   ← (需要修改)
    │
    ├── data_collector/
    │   └── agent.py   ← (保持不变)
    │
    ├── fundamental/
    │   └── agent.py   ← (新增)
    │
    ├── valuation/
    │   └── agent.py   ← (新增)
    │
    ├── risks/
    │   └── agent.py   ← (新增)
    │
    └── aggregator/
        └── agent.py   ← (新增)
```

```
Root Agent
   ↓
Planner Agent
   ↓
Data Collector Agent
   ↓
---------------------------------------
↓ Fundamental Analysis Agent
↓ Valuation Analysis Agent
↓ Risk Analysis Agent
---------------------------------------
   ↓
Aggregator Agent
   ↓
Final Markdown Report
```

## 🔧 Setup

```bash
git clone https://github.com/zhangxijing97/stock-insight.git
cd stock-insight
pip install -r requirements.txt
```

Create a `.env` file:

```bash
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=your_api_key_here
```

## ▶️ Run

### Developer UI
```bash
adk web
```

### Production API Server
```bash
adk serve
```

## 💬 Example Usage

**Price only**
```
What is the price of AAPL?
```

**Full analysis**
```
Give me a full analysis of TSLA.
```

**Ambiguous**
```
Tell me about MSFT.
```
Root agent will ask whether you want **price** or **full report**.

## 📄 Sample Output

```
## Stock Analysis Report: AAPL
**Current Price:** $183.12

### Fundamental Analysis
...

### Valuation Analysis
...

### Key Risks
...

---
Disclaimer: This is an AI-generated analysis and not financial advice.
```