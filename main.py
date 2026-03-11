from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# Load trained model
model = pickle.load(open("heart_model.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "Heart Disease Prediction API"}

@app.post("/predict")
def predict(features: list):

    data = np.array(features).reshape(1,-1)

    prediction = model.predict(data)

    return {"prediction": int(prediction[0])}