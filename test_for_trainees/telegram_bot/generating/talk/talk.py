import openai
from config import chatgpt_api_key
openai.api_key = chatgpt_api_key
messages = {}


async def generate_chat(prompt, userid):
    if userid not in messages:
        messages[userid] = []

    messages[userid].append({'role': 'system', 'content': 'You are now connected to the chat.'})
    messages[userid].append({'role': 'user', 'content': prompt})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages[userid],
        max_tokens=2500,
        temperature=0.7,
        n=1,
        stop=None,
    )

    message = response.choices[0].message
    content = message.content.strip()
    messages[userid].append({'role': 'assistant', 'content': content})

    return content
