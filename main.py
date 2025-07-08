from fastapi import FastAPI
from typing import List

app = FastAPI()

drinks = [
    {"id": 1, "name": "Coca-Cola", "price": 8000},
    {"id": 2, "name": "Pepsi", "price": 7500},
    {"id": 3, "name": "Fanta", "price": 7700}
]

@app.get("/")
def home():
    return {"message": "Xush kelibsiz! Ichimliklar sayti"}

@app.get("/drinks")
def get_drinks():
    return {"drinks": drinks}
