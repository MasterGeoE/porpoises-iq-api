from fastapi import FastAPI
from routes import api

app = FastAPI()

app.include_router(api.router)

@app.get('/')
def root():
    return {"return":"error"}
