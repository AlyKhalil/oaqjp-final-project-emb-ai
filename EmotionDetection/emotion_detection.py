import requests
import json

def emotion_detector(text_to_analyse):
    base_url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_obj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(base_url, json = json_obj, headers = header)

    if response.status_code == 400 or response.status_code == 500:
        return{
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)['emotionPredictions'][0]['emotion']

    return{
        'anger': formatted_response['anger'],
        'disgust': formatted_response['disgust'],
        'fear': formatted_response['fear'],
        'joy': formatted_response['joy'],
        'sadness': formatted_response['sadness'],
        'dominant_emotion': max(formatted_response, key=formatted_response.get)
    }
