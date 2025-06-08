import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/trigger-n8n")
def trigger_n8n_webhook():
    url = "https://n8n.srv795087.hstgr.cloud/webhook/upload"
    data = {
        "name": "Jane Doe",
        "risk": "high",
        "age": 28
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return {"n8n_response": response.json()}
    except requests.exceptions.RequestException as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
