
from cmath import pi
from typing import Optional
from fastapi import FastAPI
import pickle

app = FastAPI()

#@app.on_event("starup")
def load_model():
    global model
    model =pickle.load(open("ml_model_regression.pkl","rb"))
@app.get('/')



def index():
    return {

        "msg": "Machine learning",
        "author":"Henrry Jiménez"

    }