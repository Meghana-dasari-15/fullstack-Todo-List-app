from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

items = []

@app.get("/items")
def get_items():
    return items

@app.post("/items")
def add_item(item: dict):
    items.append(item)
    return {"message": "Item added"}
@app.delete("/items/{item_index}")
def delete_item(item_index: int):
    if 0 <= item_index < len(items):
        removed = items.pop(item_index)
        return {"message": "Item deleted", "item": removed}
    return {"error": "Invalid index"}
