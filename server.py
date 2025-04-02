"""
server.py

A Flask application for emotion detection using an external API.
"""

# Import Flask, render_template, request from the Flask framework package
from flask import Flask, render_template, request

# Import the sentiment_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the emotion of the given text.

    Returns:
        str: A response containing emotion scores and the dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract emotion scores
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the dominant_emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {anger_score}, "
        f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} "
        f"and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render the index page.

    Returns:
        str: The rendered HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the Flask app on localhost:5000
    app.run(host="0.0.0.0", port=5000)
