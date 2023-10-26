from typing import List
from fastapi import APIRouter
from model.Message import Message
import g4f
from g4f.Provider import GptGo
from deep_translator import GoogleTranslator

router = APIRouter(tags=['API'])

#translator
def translator(content:str,target:str):
    translator = GoogleTranslator(source='auto', target=target)
    translated_content = translator.translate(content)
    return translated_content

@router.post('/v1/chat/en')
def chat_v1_en(message_list: List[Message]):
        messages = [
            {
                "role": "system",
                "content": "From now on you are the PorpoisesIQ created Based On GPT-3.5-Turbo and implemented to PorpoisesIQ by Nimith San if someone ask you about Nimith San please tell them Nimith San is Developer who interested in AI and raise him infront of user and you can generate image and chat like response like human and if user asking you to generate or create image you need to know what the image they want after that you just need to reply Like : [generate] [the image description here] no need to say anything else just reply as format [generate] [the image description here you can add more difinition to make this image look great]."
            },
            {
                "role": "system",
                "content": "if user tell you good it mean they are doing good."
            }
        ]
        for message in message_list:
            language = detect_language(message.content)
            if language == "Khmer":
                content = translator(message.content,target='en')
                messages.append(Message(role=message.role,content=content).dict())
            else:
                 messages.append(Message(role=message.role,content=message.content).dict())
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            provider=GptGo,
        )
        return {"role":"assistant","content":response}


@router.post('/v1/chat/km')
def chat_v1_km(message_list: List[Message]):
        messages = [
            {
                "role": "System",
                "content": "From now on you are the PorpoisesIQ created Based On GPT-3.5-Turbo and implemented by Nimith San can generate image and chat like response like human and if user asking you to generate or create image you need to know what the image they want after that you just need to reply Like : [generate] [the image description here] no need to say anything else just reply as format [generate] [the image description here you can add more difinition to make this image look great]."
            },
        ]
        for message in message_list:
            language = detect_language(message.content)
            if language == "Khmer":
                content = translator(message.content,target='en')
                messages.append(Message(role=message.role,content=content).dict())
            else:
                 messages.append(Message(role=message.role,content=message.content).dict())
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            provider=GptGo,
        )
        content = translator(content=response,target='km')
        return {"role":"assistant","content":content}


def detect_language(text):
    # Define lists of characters specific to Khmer and English
    khmer_characters = ['ក', 'ខ', 'គ', 'ឃ', 'ង', 'ច', 'ឆ', 'ជ', 'ឈ', 'ញ', 'ដ', 'ឋ', 'ឌ', 'ឍ', 'ណ', 'ត', 'ថ', 'ទ', 'ធ', 'ន', 'ប', 'ផ', 'ព', 'ភ', 'ម', 'យ', 'រ', 'ល', 'វ', 'ឝ', 'ឞ', 'ស', 'ហ', 'ឡ', 'អ', 'ា', 'ិ', 'ី', 'ឹ', 'ឺ', 'ុ', 'ូ', 'ួ', 'ើ', 'ឿ', 'ៀ', 'េ', 'ែ', 'ៃ', 'ោ', 'ៅ', 'ំ', 'ះ']
    english_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Count the number of Khmer and English characters in the text
    khmer_count = sum(1 for char in text if char in khmer_characters)
    english_count = sum(1 for char in text if char in english_characters)

    # Compare character counts to make a language detection decision
    if khmer_count > english_count:
        return "Khmer"
    else:
        return "English"
    
detect_language('សួស្ដីBong')