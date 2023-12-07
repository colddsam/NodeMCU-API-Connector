from fastapi import FastAPI,Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import List, Dict
import json
from gspread import GspreadOeration

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

gspread=GspreadOeration()

@app.post('/')
def rootpage():
    return 'This is ESP 8266 backend fetch API'


@app.get("/connection/")
async def update_content(data: float=Query(...)):
    try:
        value=[datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),data]
        res=gspread.append_data(value)
        return {"report": res}
    except Exception as e:
        return {"report": "negative", "error": str(e)}


@app.get("/export/")
async def dataexport():
    res=gspread.show_data()
    return res

