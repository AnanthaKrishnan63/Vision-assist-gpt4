Vision Assist: Image Analysis with GPT-4

This repository contains a Django-based web application that leverages the power of OpenAI's GPT-4 Vision API to analyze and answer questions about user-uploaded images. The project serves as a "visual assistant," allowing users to gain insights from images through a simple and interactive interface.

How it Works

The application follows a straightforward user flow:

Image Upload: The user is first presented with a clean interface to upload an image directly from their device or by using their camera.

Query Input: After the image is uploaded, the user is redirected to a second page where they can type a question or a prompt related to the image.

Backend Processing: The backend, powered by Django, takes the uploaded image and resizes it for efficient processing.

AI Analysis: The resized image and the user's text prompt are sent to the OpenAI GPT-4 Vision API.

Display Results: The application receives the response from the API and displays the generated text, providing the user with an answer or description based on the visual content.

Key Features

Web-Based Interface: A simple, two-step process for uploading images and submitting questions.

Image Preprocessing: Automatically resizes images to an optimal size for API submission, ensuring faster processing.

GPT-4 Vision Integration: Directly connects to the OpenAI API to provide state-of-the-art image analysis.

Standalone Scripts: Includes separate Python scripts for:

Speech-to-Text: A script (project.py) that uses OpenAI's whisper model to transcribe audio files.

Automated Watcher: A script (test_image/automate.py) that uses watchdog to monitor a directory for new images and trigger a processing script automatically.

Tech Stack

Backend: Python, Django

Frontend: HTML, CSS

AI & Machine Learning: OpenAI API (GPT-4 Vision)

Image Processing: Pillow

API Communication: requests library

Environment Management: Pipenv

Setup and Install the repository and start to devolopment server.

Access the Application:
Open your web browser and navigate to http://127.0.0.1:8000/test_image/Vision to start using the application.

Usage

Go to the /test_image/Vision endpoint.

Use the form to upload an image and click "Upload."

On the next screen, type your question about the image into the text box.

Click "Submit" to send the image and your question to the GPT-4 Vision API.

The browser will display the answer returned by the API.

This project is a great starting point for anyone looking to build applications that bridge the gap between visual content and natural language understanding.
