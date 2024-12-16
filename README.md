Face Recognition API with Flask
A lightweight Flask-based API that compares faces from two image URLs using the face_recognition library. This API identifies whether the face in the uploaded image matches the reference image.

Features
Fetches images from URLs.
Uses face_recognition library to detect and compare faces.
Provides a simple API endpoint for face verification.
Returns clear results as Yes, Image Matched or No, Face Not Matched.
Prerequisites
Make sure you have the following installed:

Python 3.7 or above
face_recognition library
numpy, requests, Pillow
Flask


Clone the repository:

bash
Copy code
git clone https://github.com/ChethanaN/face-recognition-api.git
cd face-recognition-api

