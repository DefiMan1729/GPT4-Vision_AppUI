import base64
import requests
# import json
import gradio as gr
import tempfile
from PIL import Image
import uuid

api_key = "<read api Key from env file"

def create_upload_file(image: Image):
    # name = file.filename
    # type = file.content_type
    # image_path = name
    image_id=uuid.uuid1()
    image_path=f'{tempfile.gettempdir()}/{image_id}.png'
    image.save(image_path)
  # Function to encode the image
    def encode_image(image_path):
      with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

    # # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {api_key}"
    }

    payload = {
      "model": "gpt-4-vision-preview",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": """ identify the following from the image:
                          -type of the document
                          -document number
                          -name of the person
                          -nationality
                          -date of birth
                          Format your response as a JSON object with "document_type", "document_number", "name", "nationality", date_of_birth" as keys
                          Remove ```JSON
                          Try to identify other items and add appropriare key value pair.
                          Make your response as short as possible. If you dont identify what is asked keep the key blank.
                            """
            },
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
              }
            }
          ]
        }
      ],
      "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    # print(response.json())
    print(response.json()["choices"][0]["message"]["content"])

    return {'status':'loaded successfully, check console','output': response.json()["choices"][0]["message"]["content"]}
    return response.json()["choices"][0]["message"]["content"]

demo = gr.Interface(
   fn=create_upload_file,
   inputs = gr.components.Image(label='Input',type='pil'),
   outputs="text"
)

demo.launch()