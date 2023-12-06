from fastapi import FastAPI,Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import List, Dict
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def load_json() -> Dict:
    try:
        with open('./data.json', 'r') as lj:
            jsonfile = json.load(lj)
        return jsonfile
    except FileNotFoundError:
        return {"data": []}


def save_json(jsonfile: Dict) -> None:
    with open('./data.json', 'w') as lj:
        json.dump(jsonfile, lj)


@app.post('/')
def rootpage():
    return 'This is ESP 8266 backend fetch API'


@app.get("/connection/")
async def update_content(data: float=Query(...)):
    try:
        jsonfile = load_json()
        value = {
            "value": data,
            "date": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        }
        jsonfile['data'].append(value)
        save_json(jsonfile)
        return {"report": "positive"}
    except Exception as e:
        return {"report": "negative", "error": str(e)}


@app.get("/export/")
async def dataexport():
    res= load_json()
    return res

