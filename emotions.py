Emotion_template = {
    "cry" :{
        "triggers" : ["Monday mornings", "bad news", "sad movies", "heartbreak", "loneliness", "Empty fridge0"],
        "symptoms" : ["tears", "sobbing", "feeling of heaviness in the chest", "loss of appetite", "difficulty sleeping"],
        "metrics" : ["duration of crying episodes", "intensity of tears", "frequency of crying", "impact on daily activities", "emotional state before and after crying"]
    },
    
    "rage" :{
        "triggers" : ["traffic jams", "injustice", "disrespect", "frustration", "stressful situations"],
        "symptoms" : ["increased heart rate", "muscle tension", "clenched fists", "yelling or shouting", "feeling of heat in the body"],
        "metrics" : ["duration of rage episodes", "intensity of anger", "frequency of rage outbursts", "impact on relationships and work", "emotional state before and after rage"]
    },
    
    "happy" :{
        "triggers" : ["achieving goals", "spending time with loved ones", "receiving good news", "engaging in hobbies", "positive social interactions"],
        "symptoms" : ["smiling", "laughter", "feeling of warmth in the chest", "increased energy", "optimism"],
        "metrics" : ["duration of happiness episodes", "intensity of joy", "frequency of happy moments", "impact on overall well-being", "emotional state before and after happiness"]
    },
    
    "numb" :{
        "triggers" : ["trauma", "depression", "overwhelm", "emotional exhaustion", "coping mechanism"],
        "symptoms" : ["lack of emotional response", "feeling detached from reality", "difficulty experiencing pleasure", "loss of interest in activities", "feeling of emptiness"],
        "metrics" : ["duration of numbness episodes", "intensity of emotional detachment", "frequency of numbness", "impact on daily functioning", "emotional state before and after numbness"]
    },
    
    "anxious" :{
        "triggers" : ["uncertainty", "social situations", "performance pressure", "health concerns", "financial stress"],
        "symptoms" : ["restlessness", "rapid heartbeat", "sweating", "difficulty concentrating", "feeling of impending doom"],
        "metrics" : ["duration of anxiety episodes", "intensity of anxious feelings", "frequency of anxiety attacks", "impact on daily life and relationships", "emotional state before and after anxiety"]
    }   
}

RESPONSES = {
    "cry": [
        "Valid. Crying is just eye sweating.",
        "Tissue companies thank you for your service.",
        "Your tears have been archived.",
        "Crying: 10/10 would recommend."
    ],
    "rage": [
        "Noted. Please don't break anything expensive.",
        "Your anger fuels the chaos engine.",
        "Rage level: concerning but entertaining.",
        "Have you tried screaming into a pillow?"
    ],
    "happy": [
        "Suspicious. Are you okay?",
        "Happiness logged. Enjoy it while it lasts.",
        "Your serotonin levels are showing off.",
        "Being happy is so 2019."
    ],
    "anxious": [
        "Same tbh.",
        "Anxiety is just spicy concern.",
        "Your overthinking has been documented.",
        "Everything is fine. Probably. Maybe not."
    ],
    "numb": [
        "Felt that. Or didn't. Hard to tell.",
        "Numbness: the factory reset of emotions.",
        "You're on standby mode.",
        "Error 404: Feelings not found."
    ]
}

import random

def generate_emotion_data(emotion):
    if emotion not in Emotion_template:
        return None
    
    template  = Emotion_template[emotion]
    
    data = {
        "emotion" : emotion,
        "intensity" : random.randint(1, 10),
        "triggers" : random.choice(template["triggers"]),
        "symptoms" : random.sample(template["symptoms"], k=random.randint(1, len(template["symptoms"]))),
        "duration_minutes" : random.randint(5, 120),
        "timestamp" : None
    }
    
    for metric in template["metrics"]:
        data[metric] = random.randint(1, 10)
    
    return data

def generate_response(emotion):
    if emotion not in RESPONSES:
        return "Emotion response not found."
    
    return random.choice(RESPONSES.get(emotion, ["Response not found. Even we're confused."]))