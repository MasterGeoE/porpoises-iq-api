from typing import List
from fastapi import FastAPI
from g4f.Provider import (GptGo)
import g4f
from sdxl import ImageGenerator
import uvicorn
from model.Message import Message

app = FastAPI()

@app.get('/')
def root(): 
    return {'message':'this is PorpoisesIQ api'}

@app.post('/v1/chat')
def chat(message_list: List[Message]):
        messages = [
            {
                "role": "system",
                "content": "from now on you are the ChatBot name PorpoisesIQ created by Nimith San and you can do everything even create or generate image by using Stable Diffusion XL"
            },
            {
                "role": "system",
                "content": "when user ask you to generate image you must know what the image they want you to generate after that you just need to reply with them only [generate] [prompt image user want here] and no need to reply sure or something else!"
            }
        ]
        for message in message_list:
            messages.append(message.dict())

        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            provider=GptGo,
        )
        if "[generate]" in response:
                client = ImageGenerator()
                images = client.gen_image(response)
                return images
        return {"role":"assistant","content":response}



@app.post('/v1/image')
def image():
    client = ImageGenerator()
    images = client.gen_image("korean super man on mar with colors.")
    return images