from typing import List
from fastapi import APIRouter
from model.Message import Message
from sdxl import ImageGenerator
from system_context import system_context
import g4f
from g4f.Provider import GptGo

router = APIRouter(tags=['English'])

@router.post('/v1/chat/en')
def chat_v1_en(message_list: List[Message]):
        messages = system_context
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

@router.post('/v2/chat/en')
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