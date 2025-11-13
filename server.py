"""
Flask server for Emotion Detection web application.

This module sets up two routes:
1. '/' — renders the home page.
2. '/emotionDetector' — accepts text input and returns detected emotions. 
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector')
def emot_detection():
    """
    Endpoint to analyze emotions in a given text query parameter.

    Returns:
        str: A formatted string describing emotion scores and dominant emotion
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route('/')
def render_index_page():
    """
    Renders the application's main index page.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
