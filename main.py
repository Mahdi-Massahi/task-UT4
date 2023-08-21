from fastapi import FastAPI
from datetime import date

app = FastAPI()

@app.get('/')
def get_current_date():
    return {'date': str(date.today())}

@app.get('/greet/{name}')
def greet_user(name: str):
    return {'message': f'Hello, {name}!'}
import pandas as pd

# Read the CSV file
data = pd.read_csv("data.csv")

# Remove duplicates
data = data.drop_duplicates()

# Fill missing values
data = data.fillna(0)

# Convert dates
data["date"] = pd.to_datetime(data["date"])

# Save the cleaned data to a new CSV file
data.to_csv("cleaned_data.csv", index=False)
