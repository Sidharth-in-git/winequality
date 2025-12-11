from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import os
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model safely
model_path = os.path.join(os.path.dirname(__file__), "wine_model.pkl")
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
except Exception as e:
    print("Error loading model:", e)
    model = None

# Define input schema
class WineData(BaseModel):
    alcohol: float
    density: float
    pH: float

# Prediction endpoint
@app.post("/predict")
def predict_wine_quality(data: WineData):
    if model is None:
        return {"error": "Model not loaded"}
    try:
        # Map input to correct column names used in training
        df = pd.DataFrame([{
            "alcohol": data.alcohol,
            "density": data.density,
            "pH": data.pH  # changed from volatile acidity to pH
        }])
        prediction = model.predict(df)[0]
        return {"predicted_quality": round(float(prediction), 2)}
    except Exception as e:
        return {"error": str(e)}
