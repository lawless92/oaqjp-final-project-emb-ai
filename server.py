from flask import Flask,render_template,jsonify,request
from EmotionDetection import emotion_detection


app = Flask(__name__)

@app.route('/')

def home_page():
    """ render the home page """
    return render_template('index.html')


@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get("textToAnalyze", "").strip()
    if not text:
        return jsonify({"error": "Introduce un texto para analizar"}), 400

    return jsonify(emotion_detection.emotion_detector(text))


app.run(debug=True)