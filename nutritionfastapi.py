import requests
from fastapi import FastAPI

app = FastAPI()

@app.post("/trigger-n8n")
def trigger_n8n_webhook():
    url = "https://n8n.srv795087.hstgr.cloud/webhook/upload"
    data = {
        "name": "Jane Doe",
        "risk": "high",
        "age": 28
    }
    response = requests.post(url, json=data)
    return {"n8n_response": response.json()}
