import os
import glob
import whisper 
from PIL import Image
import base64
import requests

def gptout(txt):
  out_ans = None
  #to get the latest file
  list_of_files = glob.glob(r'..\media\images\*') # * means all if need specific format then *.csv
  latest_file = max(list_of_files, key=os.path.getctime)
  #print(repr(latest_file))

  str=latest_file[26:]
  path = latest_file[:26]
  #print(repr(path))
  #print(str)
  point_pos = str.find('.')
  file_name = str[:point_pos]
  ext = str[point_pos:]
  file = file_name + "_resized" + ext
  #print(file)
  absolute_path = "path_to_save_photos_here"+file
  #print(repr(absolute_path))

  #TO RESIZE THE IMAGE
  def imgresize():
      im = Image.open(latest_file)
      x=im.size[0]
      y=im.size[1]
      mf0=512/x
      mf1=512/y
      resized_im = im.resize((round(im.size[0]*mf0), round(im.size[1]*mf1)))
  #Save the cropped image
      resized_im.save(absolute_path)

  imgresize()

  #GPT4-Vision_api

  # OpenAI API Key
#  api_key = ""

  def encode_image(image_path):
    with open(image_path, "rb") as image_file:
      return base64.b64encode(image_file.read()).decode('utf-8')

  # Path to your image
  image_path = absolute_path

  # Getting the base64 string
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
            "text": txt
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
    "max_tokens": 1000
  }

  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
  out_ans = response.json()['choices'][0]['message']['content']
  return out_ans


