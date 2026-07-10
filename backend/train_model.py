import pandas as pd

data = pd.read_csv("../dataset/Symptom2Disease.csv")

print(data.head())
print(data.columns)
print(data.shape)