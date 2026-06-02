import requests
import json

def emotion_detector(text_to_analyse):
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)
    
    if response.status_code == 200:
        # Parsing the JSON response from the API
        formatted_response = response.json()

        emotion_data = formatted_response["emotionPredictions"][0]["emotion"]

        anger_score = emotion_data["anger"]
        disgust_score = emotion_data["disgust"]
        fear_score = emotion_data["fear"]
        joy_score = emotion_data["joy"]
        sadness_score = emotion_data["sadness"]

        dominant_emotion = max(emotion_data, key=emotion_data.get)
    else:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    return result
