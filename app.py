from fastapi import FastAPI
import uvicorn
import sys
import os
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from pydantic import BaseModel  # Added for request body validation
from textSummarizer.components.prediction import PredictionPipeline

app = FastAPI()

# Define the structure of the incoming JSON data


class PredictionRequest(BaseModel):
    text: str


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        # Running the main.py training script
        os.system("python main.py")
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/predict")
async def predict_route(request: PredictionRequest):
    try:
        # Instantiate the pipeline for your NLP project
        obj = PredictionPipeline()

        # Access the text from the validated request body
        summary = obj.predict(request.text)
        return summary

    except Exception as e:
        # Providing a descriptive error response for debugging
        return Response(f"Error Occurred! {e}", status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
