import requests

def emotion_detector(text_to_analyse):
    base_url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_obj = { "raw_document": { "text": text_to_analyse } }

    response  = requests.post(base_url, json = json_obj, headers = headers)

    return response.text
