from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/predict")
def predict():
    return jsonify({
        "disease": "Not Predicted Yet",
        "causes": "AI model not connected",
        "remedies": "Will be added in Day 3",
        "status": "API Working"
    })

if __name__ == "__main__":
    app.run(debug=True)