# Data Dictionary

## Dataset Name
Disease Prediction Using Machine Learning

## Input Features
The dataset contains symptom columns as input features.

### Symptom Columns
- Each symptom represents a possible disease symptom.
- Values:
  - 0 → Symptom absent
  - 1 → Symptom present

Examples:
- itching
- skin_rash
- fever
- cough
- headache
- fatigue
(etc.)

## Output Column

### prognosis
- This is the target variable.
- It represents the disease predicted by the machine learning model.
- The model learns the relationship between symptoms and the corresponding disease.

## Dataset Files

### Training.csv
- Used for training the machine learning model.
- Contains symptom data and corresponding disease labels.

### Testing.csv
- Used for testing model performance.
- Contains symptom data for prediction evaluation.