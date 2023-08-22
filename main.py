from fastapi import FastAPI
from datetime import date

app = FastAPI()

@app.get("/")
def get_current_date():
    return {"current_date": str(date.today())}
