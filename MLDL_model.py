import io
import os
import sys
import recognize_speech_from_mic
import speech_recognition as sr
from PIL import Image, ImageDraw
from google.cloud import vision # Imports the Google Cloud client library

from threading import Timer
timer = Timer(5, print, '')

# Set environment variable
credential_path = "/Users/honghanbyul/Documents/발버둥/GDSC/IDEATON/EYE-KEY/MLDL_STT/eyekey-OCR.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('/Users/honghanbyul/Documents/발버둥/GDSC/IDEATON/EYE-KEY/MLDL_STT/lott.jpeg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)
img = Image.open('lott.jpeg').convert('RGB') # 사진은 .. 앱에서 촬영한 이미지로 받아오도록 바꿔야 함

# Performs text detection on the image file
response = client.text_detection(image=image)
texts = response.text_annotations

search = recognize_speech_from_mic.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone(device_index=1))
timer.start()
#print(search)

while 'Error' in search:
    sys.exit('Error')

first_array = []
second_array = []
third_array = []
fourth_array = []

for text in texts:
    vertices = (['({},{})'.format(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices])
    if text.description in search:
        right_up, left_down = vertices[1], vertices[3]
        first_array.append(int(right_up[1:4]))
        second_array.append(int(right_up[5:8]))
        third_array.append(int(left_down[1:4]))
        fourth_array.append(int(left_down[5:8]))

while len(first_array) == 0:
    sys.exit('검색 결과가 없습니다.')

draw = ImageDraw.Draw(img)

for i in range(len(first_array)):
    bound = [first_array[i], second_array[i], third_array[i], fourth_array[i]]
    draw.rectangle((bound), outline=(255,0,0), width = 3)

    img.show()