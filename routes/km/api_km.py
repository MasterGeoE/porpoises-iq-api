from typing import List
from deep_translator import GoogleTranslator
from fastapi import APIRouter
from model.Message import Message
from sdxl import ImageGenerator
from system_context import system_context
import g4f
from g4f.Provider import GptGo

router = APIRouter(tags=["Khmer"])

def translator(content:str,target:str):
        translator = GoogleTranslator(source='auto', target=target)
        content_translated = translator.translate(content)
        return content_translated
      
@router.post('/v1/chat/km')
def chat_v1_km(message_list: List[Message]):
        messages = [
            {
                "role": "system",
                "content": "From now on you are the chatbot can generate image and chat like response like human and if user asking you to generate or create image you need to know what the image they want after that you just need to reply Like : [generate] [the image description here] no need to say anything else just reply as format [generate] [the image description here you can add more difinition to make this image look great]."
            },
        ]
        for message in message_list:
            content = translator(content=message.content,target='en')
            messages.append(
                Message(
                       role=message.role,
                       content=content
                ).dict()
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
        content = translator(content=response,target='km')
        return {"role":"assistant","content":content}


@router.post('/v2/chat/km')
def chat_v2_km(message_list: List[Message]):
        messages = [
            {
                "role": "system",
                "content": "From now on you are the chatbot can generate image and chat like response like human and if user asking you to generate or create image you need to know what the image they want after that you just need to reply Like : [generate] [the image description here] no need to say anything else just reply as format [generate] [the image description here you can add more difinition to make this image look great]."
            },
        ]
        for message in message_list:
            content = translator(content=message.content,target='en')
            messages.append(
                Message(
                       role=message.role,
                       content=content
                ).dict()
            )

        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            provider=GptGo,
        )
        content = translator(content=response,target='km')
        return {"role":"assistant","content":content}

@router.post('/v2/image/km')
def image_v2_km(prompt:str):
        client = ImageGenerator()
        images = client.gen_image(prompt=prompt)
        return images


