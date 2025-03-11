from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

app = FastAPI()



# Load the model and scaler
scaler = joblib.load("scaler.joblib")
model = joblib.load("kmeans.joblib")


# Define request schema
class PlayerStats(BaseModel):
    appearance: int
    minutes_played: int
    award: int
    current_value: int
    highest_value: int



app = FastAPI()

@app.post("/predict")
def predict(data: PlayerStats):
    # Convert input to DataFrame with column names
    input_df = pd.DataFrame([data.dict()])  

    # Scale the input
    scaled_input = scaler.transform(input_df)

    # Make prediction
    prediction = model.predict(scaled_input)

    # Convert NumPy int32 to Python int
    return {"cluster": int(prediction[0])}
