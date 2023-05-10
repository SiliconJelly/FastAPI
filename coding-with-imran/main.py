from typing import Union  # class
from fastapi import FastAPI  # class
import random as rd

app = FastAPI()  # creates a new object


items = {
    "1": {"name": "Foo", "price": 50.2},
    "2": {"name": "Bar", "price": 62},
    "3": {"name": "Baz", "price": 50.8},
    "4": {"name": "Too", "price": 54.3},
    "5": {"name": "Boo", "price": 20.6},
}

# endpoint in postman: http://localhost:5000/item
@app.get("/item")
async def read_item():
    random_key = rd.choice(list(items.keys())) ## randomly selecting a key in items
    random_value = items[random_key]  ## calling the value of the selected key
    return {"message": random_value}  ## returning the value

# endpoint in postman: http://localhost:5000/items 
@app.get("/items")
async def read_items():
    return items     ## returning all the value

# start the app (in case, path known) → uvicorn main:app --port 5000 --reload --log-level debug
# my terminal couldn't find the path, so I had to tell python with python -m (rest of the script) →
# python -m uvicorn main:app --port 5000 --reload --log-level debug


@app.get("/")
def read_root():
    return {"Hello from FastAPI"}


'''
Expected Output:
INFO:     Will watch for changes in these directories: ['C:\\Users\\SiliconJelly\\Desktop\\Projects\\coding-with-imran']
INFO:     Uvicorn running on http://127.0.0.1:5000 (Press CTRL+C to quit)
INFO:     Started reloader process [3764] using WatchFiles
INFO:     Started server process [16740]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
'''
