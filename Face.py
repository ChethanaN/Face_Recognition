from flask import Flask, jsonify, request

app = Flask(__name__)

import requests
import cv2
import face_recognition
import numpy as np
from PIL import Image
from io import BytesIO


def load_image_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return np.array(image.convert("RGB"))
    else:
        raise ValueError("Unable to fetch the image. Check the URL.")




def identify_face_from_url(uploaded_image_url, anotherimage):

    your_image_url = anotherimage
    your_image = load_image_from_url(your_image_url)
    your_face_encodings = face_recognition.face_encodings(your_image)

    if len(your_face_encodings) == 0:
        raise RuntimeError("No face detected in the reference image.")
    your_face_encoding = your_face_encodings[0]


    uploaded_image = load_image_from_url(uploaded_image_url)


    face_locations = face_recognition.face_locations(uploaded_image)
    face_encodings = face_recognition.face_encodings(uploaded_image, face_locations)

    if not face_encodings:
        return "No face detected in the uploaded image."

    for face_encoding in face_encodings:

        matches = face_recognition.compare_faces([your_face_encoding], face_encoding)


        if matches[0]:
            return "Yes, Image Matched"
        else:
            return f"No, Face Not Matched"
    return "Face identification completed."

@app.route('/')
def hello():
    url1 = request.args.get('url1', 'Unknown')
    url2 = request.args.get('url2', 'Unknown')
    uploaded_image_url = url1
    result = identify_face_from_url(uploaded_image_url,url2)
    return result

if _name_ == '__main__':
    app.run()
