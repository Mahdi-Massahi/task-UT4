from fastapi import FastAPI
from datetime import date
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.post("/")
def get_current_date():
    logging.info('Received POST request')
    return {"current_date": str(date.today())}
