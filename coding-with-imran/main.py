# a simple FastAPI web application with a single
# route that handles GET requests to the root URL

from typing import Union  # class
from fastapi import FastAPI  # class

app = FastAPI()  # creates a new object


@app.get("/")  # GET request is made to the root URL ("/")
def read_root():
    return {"Hello from FastAPI"}


# after running uvicorn, we should be getting:
'''
INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO: Started reloader process [12345]
INFO: Started server process [12346]
INFO: Waiting for application startup.
INFO: Application startup complete.
'''

# and here is the auto-generated documentation:
# http://127.0.0.1:8000/docs#/default/read_root__get
