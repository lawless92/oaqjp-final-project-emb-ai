import requests

url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

def emotion_detector(text_to_analyze):
    """Detect emotion in a given text using the Watson Emotion API."""
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, timeout=30, headers=headers, json=payload)
    response.raise_for_status()
    response_json = response.json()

    emotions = response_json["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)

    result = {
        'anger': emotions.get('anger', 0.0),
        'disgust': emotions.get('disgust', 0.0),
        'fear': emotions.get('fear', 0.0),
        'joy': emotions.get('joy', 0.0),
        'sadness': emotions.get('sadness', 0.0),
        'dominant_emotion': dominant_emotion
    }
    return result

if __name__ == "__main__":
    text_to_analyze = input("Enter the text to analyze for emotion: ")
    print(emotion_detector(text_to_analyze))