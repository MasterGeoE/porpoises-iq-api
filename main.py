from fastapi import FastAPI, Request
from routes import api
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.include_router(api.router)

templates = Jinja2Templates(directory="templates") 

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})