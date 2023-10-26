from typing import List
from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates
from routes import api

app = FastAPI()

app.include_router(api.router)


templates = Jinja2Templates(directory="templates") 

@app.get('/')
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host= "0.0.0.0", port=80)