import openai
from config import chatgpt_api_key
openai.api_key = chatgpt_api_key
async def generate_text(prompt, temperature, max_tokens):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You're the best AI Helper for users"},
        {"role": "user", "content": f"{prompt}"}],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
        )
    message = response["choices"][0]["message"]["content"].strip()
    return(message)