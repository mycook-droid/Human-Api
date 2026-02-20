import random
from emotions import generate_emotion_data, Emotion_template, RESPONSES, generate_response
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "api_name": "HUMAN API - Mood as a Service",
        "version": "1.0",
        "tagline": "Serving emotions like coffee, but more chaotic",
        "endpoints": {
            "GET /api/emotion": "List all available emotions",
            "GET /api/{emotion}": "Get data for specific emotion (cry, rage, happy, anxious, numb)",
            "GET /api/random": "Get a random emotion (you didn't choose this)",
            "GET /api/vibe-check": "Check your vibe score (1-100)",
            "POST /api/submit": "Submit your current emotion with JSON body"
        },
        "examples": [
            "/api/cry",
            "/api/random",
            "/api/vibe-check"
        ],
        "post_example": {
            "url": "/api/submit",
            "method": "POST",
            "body": {"emotion": "cry", "intensity": 8, "note": "Monday"}
        },
        "warning": "Side effects may include self-awareness and existential dread"
    })


@app.route('/api/emotion', methods=['GET'])
def list_emotion():
    emotion_list = list(Emotion_template.keys())
    return jsonify({"Available Emotions": emotion_list,
                    "total": len(emotion_list),
                    "Usage": "Use /api/<emotion_name> to get data for a specific emotion"})
    
@app.route('/api/<emotion_name>', methods=['GET'])
def get_emotion(emotion_name):
    data = generate_emotion_data(emotion_name)
    if data is None:
        return jsonify({"error": "Emotion not found",
                        "message": f"Emotion '{emotion_name}' is not available in the system"}), 404
    data["timestamp"] = datetime.now().isoformat()
    data["response"] = generate_response(emotion_name)
    
    return jsonify(data)

@app.route('/api/submit', methods=['POST'])
def submit_emotion():
    data = request.get_json()
    
    if not data or "emotion" not in data:
        return jsonify({"error": "Invalid data",
                        "message": "Please provide an 'emotion' field in the JSON body",
                        "usage": "POST with JSON: {\"emotion\": \"cry\", \"intensity\": 8, \"note\": \"optional\"}"}), 400  
    
    emotion = data.get('emotion')
    intensity = data.get('intensity', random.randint(1, 10))
    note = data.get('note', '')
    
    return jsonify({"message": "Emotion data submitted successfully",
                    "status": "Recieved",
                    "submitted_data": {
                        "your_emotion": emotion,
                        "intensity": intensity,
                        "note": note, 
                        "timestamp": datetime.now().isoformat(),    
                        "response": generate_response(emotion)
                    }
            }), 201
    
@app.route('/api/random', methods=['GET'])
def random_emotion():
    emotion_name = random.choice(list(Emotion_template.keys()))
    data = generate_emotion_data(emotion_name)
    data["timestamp"] = datetime.now().isoformat()
    data["server_response"] = generate_response(emotion_name)
    data["note"] = "You didn't choose this. It chose you."
    
    return jsonify(data)

@app.route('/api/vibe-check', methods=['GET'])
def vibe_check():
    vibe_score = random.randint(1, 100)
    
    if vibe_score < 30:
        verdict = "Vibe: Terrible. Please reboot."
    elif vibe_score < 60:
        verdict = "Vibe: Questionable. Proceed with caution."
    elif vibe_score < 85:
        verdict = "Vibe: Acceptable. You're doing fine."
    else:
        verdict = "Vibe: Immaculate. You're on fire."
    
    return jsonify({
        "vibe_score": vibe_score,
        "verdict": verdict,
        "timestamp": datetime.now().isoformat(),
        "disclaimer": "This is completely random. Don't take it seriously."
    })

if __name__ == '__main__':
    app.run(debug=True)