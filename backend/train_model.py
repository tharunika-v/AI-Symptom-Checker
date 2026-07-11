import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score


# 1. Load dataset
data = pd.read_csv("../dataset/Symptom2Disease.csv")

print(data.head())
print(data.columns)
print(data.shape)


# 2. Separate input and output

X = data["text"]       # Symptoms description
y = data["label"]      # Disease name


# 3. Encode disease labels

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)


# 4. Split data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)


# 5. Convert symptoms text into numbers

vectorizer = TfidfVectorizer()

X_train_vector = vectorizer.fit_transform(X_train)

X_test_vector = vectorizer.transform(X_test)


# 6. Train model

model = MultinomialNB()

model.fit(X_train_vector, y_train)


# 7. Test accuracy

prediction = model.predict(X_test_vector)

accuracy = accuracy_score(y_test, prediction)

print("Model Accuracy:", accuracy)


# 8. Save model files

joblib.dump(model, "../model/model.pkl")

joblib.dump(vectorizer, "../model/vectorizer.pkl")

joblib.dump(encoder, "../model/encoder.pkl")


print("Model, Vectorizer and Encoder saved successfully!")