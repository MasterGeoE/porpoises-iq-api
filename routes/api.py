from typing import List
from fastapi import APIRouter
from model.Message import Message
from sdxl import ImageGenerator
from system_context import system_context
import g4f
from g4f.Provider import GptGo

router = APIRouter(tags=['API'])

@router.post('/v1/chat')
def chat_v1_km(message_list: List[Message]):
        messages = [
            {
                "role": "system",
                "content": "From now on you are the chatbot can generate image and chat like response like human and if user asking you to generate or create image you need to know what the image they want after that you just need to reply Like : [generate] [the image description here] no need to say anything else just reply as format [generate] [the image description here you can add more difinition to make this image look great]."
            },
        ]
        for message in message_list:
            messages.append(
                message.dict()
            )

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


@router.post('/v2/chat')
def chat_v2_en(message_list:List[Message]):
        messages = system_context
        for message in message_list:
            messages.append(message.dict())

        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            provider=GptGo,
        )
        return {"role":"assistant","content":response}