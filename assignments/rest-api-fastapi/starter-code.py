# starter-code.py
# Démarrage pour le devoir FastAPI

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Route GET /hello
@app.get("/hello")
def hello():
    return {"message": "Hello, world!"}

# Route GET /greet/{name}
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

# Modèle pour POST /items
class Item(BaseModel):
    name: str

# Route POST /items
@app.post("/items")
def create_item(item: Item):
    return {"received": item.name}

# Pour lancer :
# uvicorn starter-code:app --reload
