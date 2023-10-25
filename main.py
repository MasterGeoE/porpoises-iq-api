from typing import List
from fastapi import FastAPI, Request
from g4f.Provider import (GptGo)
import g4f
from sdxl import ImageGenerator
import uvicorn
from model.Message import Message
from fastapi.templating import Jinja2Templates
from system_context import system_context
from routes.en import api_en
from routes.km import api_km

app = FastAPI()
#English
app.include_router(api_en.router)
#Khmer
app.include_router(api_km.router)


templates = Jinja2Templates(directory="templates") 

@app.get('/')
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/v2/image')
def image(prompt:str):
    client = ImageGenerator()
    images = client.gen_image(prompt)
    return images

if __name__ == "__main__":
    uvicorn.run(app, host= "192.168.12.161", port=10000)