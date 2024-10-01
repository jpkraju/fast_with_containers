# main.py
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"He1llo": "World..."}

@app.get("/test")
def get_test():
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return {"test_on": dt_string}
