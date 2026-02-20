# HUMAN API - Mood as a Service 🎭

**Tagline:** Serving emotions like coffee, but more chaotic.

An absurd REST API that turns human emotions into JSON responses. Because why not?

---

## What is this?

An API that serves random emotional data with chaotic responses. Each emotion comes with triggers, symptoms, intensity metrics, and sarcastic server commentary.

**Available Emotions:** cry, rage, happy, anxious, numb

---

## Installation
```bash
# Clone the repo
git clone https://github.com/mycook-droid/human-api.git
cd human-api

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

Server runs at: `http://127.0.0.1:5000`

---

## API Endpoints

### 1. Home - API Documentation
```bash
GET /
```
Shows all available endpoints and usage examples.

**Example Response:**
```json
{
  "api_name": "HUMAN API - Mood as a Service",
  "version": "1.0",
  "endpoints": {...}
}
```

---

### 2. List All Emotions
```bash
GET /api/emotion
```

**Example Response:**
```json
{
  "Available Emotions": ["cry", "rage", "happy", "anxious", "numb"],
  "total": 5
}
```

---

### 3. Get Specific Emotion Data
```bash
GET /api/{emotion}
```

**Example:**
```bash
curl http://127.0.0.1:5000/api/cry
```

**Response:**
```json
{
  "emotion": "cry",
  "intensity": 7,
  "triggers": "Monday mornings",
  "symptoms": ["tears", "sobbing"],
  "duration_minutes": 45,
  "duration of crying episodes": 8,
  "intensity of tears": 6,
  "timestamp": "2025-02-21T10:30:00",
  "response": "Valid. Crying is just eye sweating."
}
```

---

### 4. Random Emotion Generator
```bash
GET /api/random
```
Returns a completely random emotion. You don't choose it, it chooses you.

**Example:**
```bash
curl http://127.0.0.1:5000/api/random
```

---

### 5. Vibe Check
```bash
GET /api/vibe-check
```
Gives you a random vibe score from 1-100. Completely meaningless but fun.

**Example Response:**
```json
{
  "vibe_score": 73,
  "verdict": "Vibe: Acceptable. You're doing fine.",
  "timestamp": "2025-02-21T10:30:00",
  "disclaimer": "This is completely random. Don't take it seriously."
}
```

---

### 6. Submit Your Emotion
```bash
POST /api/submit
Content-Type: application/json
```

**Request Body:**
```json
{
  "emotion": "rage",
  "intensity": 9,
  "note": "Traffic was terrible"
}
```

**Example Command:**
```bash
curl -X POST http://127.0.0.1:5000/api/submit \
  -H "Content-Type: application/json" \
  -d '{"emotion":"cry","intensity":8,"note":"Monday blues"}'
```

**Response:**
```json
{
  "message": "Emotion data submitted successfully",
  "status": "Received",
  "submitted_data": {
    "your_emotion": "cry",
    "intensity": 8,
    "note": "Monday blues",
    "timestamp": "2025-02-21T10:30:00",
    "response": "Tissue companies thank you for your service."
  }
}
```

---

## Quick Test All Endpoints
```bash
# 1. Home
curl http://127.0.0.1:5000/

# 2. List emotions
curl http://127.0.0.1:5000/api/emotion

# 3. Get cry data
curl http://127.0.0.1:5000/api/cry

# 4. Get rage data
curl http://127.0.0.1:5000/api/rage

# 5. Random emotion
curl http://127.0.0.1:5000/api/random

# 6. Vibe check
curl http://127.0.0.1:5000/api/vibe-check

# 7. Submit emotion
curl -X POST http://127.0.0.1:5000/api/submit \
  -H "Content-Type: application/json" \
  -d '{"emotion":"happy","intensity":10,"note":"Got coffee"}'
```

---

## Deployment

### Deploy to Render
1. Push code to GitHub
2. Go to render.com → New Web Service
3. Connect your repo
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `gunicorn app:app`

---

## Tech Stack
- **Python 3.x**
- **Flask** - Web framework
- **Gunicorn** - Production server

---

## Warning ⚠️
Side effects may include self-awareness, existential dread, and an unhealthy relationship with JSON.

---

## License
Do whatever you want with this. It's chaos anyway.

---

## Author
**Mohd Zishan**
- GitHub: [@mycook-droid](https://github.com/mycook-droid)
- LinkedIn: [mohd-zishan79](https://linkedin.com/in/mohd-zishan79)