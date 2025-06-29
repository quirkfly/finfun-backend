# 📊 AI Expense Forecaster & Assistant (Flask Backend)

This is a Python + Flask backend application that helps clients **forecast their expenses** based on historical transactions  
and chat with an **AI assistant powered by OpenAI GPT-4**.  
The assistant can mix serious predictions, fun replies, jokes, and financial trivia based on conversation context.

---

## 🚀 Features

✅ Forecast client's expenses using Prophet  
✅ Chat assistant that blends predictions + friendly small talk  
✅ Automatic detection when user wants a forecast vs fun mode  
✅ REST API ready to integrate with React frontend  
✅ PostgreSQL support via SQLAlchemy ORM

---

## 🏗️ Project Structure

```
app/
├── __init__.py
├── models.py
├── ml/
│   └── forecaster.py
├── services/
│   └── assistant.py
└── routes/
    └── assistant.py
```

---

## ⚙️ Setup

1. **Clone the repository**
```bash
git clone https://github.com/your-repo/expense-forecast-backend.git
cd expense-forecast-backend
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set environment variables**
```bash
export OPENAI_API_KEY=your_openai_api_key
export FLASK_APP=run.py
export FLASK_ENV=development
```

5. **Run the app**
```bash
flask run
```

---

## 📦 Dependencies

- Flask
- SQLAlchemy
- Prophet
- OpenAI Python SDK
- pandas

(See `requirements.txt`)

---

## 🧠 How it works

- The assistant **analyzes conversation**:
  - If the user message suggests wanting an expense prediction, it fetches past transactions, runs Prophet, and returns forecast.
  - Otherwise, the assistant generates a fun reply (small talk, jokes, trivia, etc.) using GPT-4.
- All logic is in `app/services/assistant.py`

---

## 📡 API

### `POST /api/assistant/chat`

Request:
```json
{
  "client_id": 1,
  "messages": [
    {"role": "user", "message": "Hey, can you forecast my expenses for next month?"}
  ]
}
```

Response:
```json
{
  "reply": "My forecast: Estimated expenses on 2025-07-27 are approximately 199.93 EUR."
}
```

---

## 🧪 Example curl requests

### 🧮 Forecast intent
```bash
curl -X POST http://127.0.0.1:5000/api/assistant/chat \
  -H "Content-Type: application/json" \
  -d '{
    "client_id": 1,
    "messages": [
      {"role": "user", "message": "Hey, can you forecast my expenses for next month?"}
    ]
  }'
```

### 😄 Fun / small talk
```bash
curl -X POST http://127.0.0.1:5000/api/assistant/chat \
  -H "Content-Type: application/json" \
  -d '{
    "client_id": 1,
    "messages": [
      {"role": "user", "message": "Tell me something funny about money!"}
    ]
  }'
```

---

## ✅ License

MIT

---

## ✏️ Author

> Built with ❤️ by quirkfly /with AI assistence/
