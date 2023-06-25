import openai
from config import chatgpt_api_key
import requests


async def generate_img(prompt):
    openai.api_key = chatgpt_api_key

    model = "image-alpha-001"
    response_format = "url"
    response = openai.Image.create(prompt=prompt, model=model, response_format=response_format, n=1, size='1024x1024')
    image_url = response["data"][0]["url"]
    response = requests.get(image_url)

    return image_url


# async def generate_img(prompt):
#     openai.api_key = chatgpt_api_key
#
#     model = "image-alpha-001"
#     response_format = "url"
#     response = openai.Image.create(prompt=prompt, model=model, response_format=response_format, n=1)
#     image_url = response["data"][0]["url"]
#
#     response = requests.get(image_url)
#     r = requests.post(
#         "https://api.deepai.org/api",
#         data={
#             'image': f'{image_url}',
#         },
#         headers={'api-key': 'e2054886-1cc7-41b8-a3cf-ecd6cef33466'}
#     )
#     # response = requests.get(r.json()["output_url"])
#     print(r.json())
#
#     return image_url





# async def generate_img(prompt):
#     openai.api_key = chatgpt_api_key
#
#     model = "image-alpha-001"
#     response_format = "url"
#     response = openai.Image.create(prompt=prompt, model=model, response_format=response_format, n=1)
#     image_url = response["data"][0]["url"]
#
#     image_response = requests.get(image_url)
#
#     temp_filename = "temp.jpg"
#     with open(temp_filename, "wb") as file:
#         file.write(image_response.content)
#
#     png_filename = "image.png"
#     image = Image.open(temp_filename)
#     image.save(png_filename, "PNG")
#
#     response = openai.Image.create_edit(
#         prompt=prompt,
#         model=model,
#         response_format=response_format,
#         n=1,
#         image=png_filename,
#         mask=png_filename,
#     )
#     image_upscale = response["data"][0]["png"]
#
#     with open(image_upscale, "rb") as file:
#         image_content = file.read()
#
#     os.remove(temp_filename)
#     os.remove(png_filename)
#
#     return image_content






