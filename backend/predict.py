import joblib

model = joblib.load("../model/model.pkl")
vectorizer = joblib.load("../model/vectorizer.pkl")
encoder = joblib.load("../model/encoder.pkl")
def predict_disease(symptoms):
    symptoms_vector = vectorizer.transform([symptoms])

    prediction = model.predict(symptoms_vector)

    disease = encoder.inverse_transform(prediction)

    return disease[0]
print(predict_disease("fever headache cough"))