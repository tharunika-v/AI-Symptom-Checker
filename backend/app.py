from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib


app = Flask(__name__)

CORS(app)


# Load ML files
model = joblib.load("../model/model.pkl")
vectorizer = joblib.load("../model/vectorizer.pkl")
encoder = joblib.load("../model/encoder.pkl")


# Test route
@app.route("/")
def home():
    return "Backend is running!"


# Prediction route
@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    symptoms = data["symptoms"]


    # Convert text into numbers
    vector = vectorizer.transform([symptoms])


    # Predict disease number
    prediction = model.predict(vector)


    # Convert number back to disease name
    disease = encoder.inverse_transform(prediction)


    return jsonify({
        "disease": disease[0]
    })


if __name__ == "__main__":
    app.run(debug=True)