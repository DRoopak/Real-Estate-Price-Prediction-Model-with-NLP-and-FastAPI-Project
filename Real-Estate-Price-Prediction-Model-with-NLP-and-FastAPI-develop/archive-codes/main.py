from fastapi import FastAPI
from typing import Any, Dict, Optional, Union

app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello !! Welcome to the Real Estate Prediction Model"}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None]=None):
    return {'item_id': item_id, "q": q}