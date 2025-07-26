HematoVision – Advanced Blood Cell Classification Using Transfer Learning
_____________________________________________________________________________________________________________________________________________________________________________________________________________________
Developed By: Siva Meghana Srikaram and Team

Project Overview
-----------------
HematoVision is a Flask-based web application that classifies microscopic blood cell images into four categories: monocyte, neutrophil, eosinophil, and lymphocyte. It uses a pre-trained transfer learning model to assist in medical diagnostics with accurate predictions.

Tech Stack
-----------
Frontend: HTML, CSS (Milligram CSS framework), Jinja2
Backend: Python, Flask
Machine Learning: TensorFlow / Keras (Transfer Learning)
Image Processing: OpenCV
Utilities: NumPy, base64, Werkzeug

Tools and Technologies
-----------------------
Jupyter Notebook: For data exploration, preprocessing, and model training
Visual Studio Code: Code development and debugging environment
Flask: Web framework for building the application
TensorFlow/Keras: Transfer learning framework for model building
OpenCV: Image processing library

Dataset:-
-------
The dataset consists of labeled microscopic images of blood cells, categorized into the following classes:
Monocyte
Neutrophil
Eosinophil
Lymphocyte
These images were used to train the transfer learning model (Blood Cell.keras) to accurately classify new blood cell images.

Functionality Overview:-
-----------------------
Upload image via web interface.
Image is converted to grayscale, resized, normalized, and flattened.
Transfer learning model (Blood Cell.keras) predicts the class.
Displays predicted label and image on result page.

Model Details
-------------
Model File: Blood Cell.keras
Input: 28x28 grayscale image (flattened to 784)
Output Classes: Monocyte, Neutrophil, Eosinophil, Lymphocyte
Frontend Templates
----------------
home.html:
A simple upload interface that allows users to upload a blood cell image.
result.html:
Displays the predicted blood cell type and shows the uploaded image using base64 encoding.

Project Structure
-----------------
project/
├── static                 # Temporary image storage 
├── templates  
│   ├── home.html           # Upload interface  
│   └── result.html         # Display result  
├── app.py                   # Main backend logic 
    ├── BloodCells.ipynb
    ├── Bloodcells.h5
  
How to Run
--------------
1.Run the Flask application:
python app.py

2.Open your browser and visit:
http://127.0.0.1:5000/

Submission Details
-------------------
Submitted By: Siva Meghana Srikaram and Team
College: Rise Krishna Sai Prakasam Group of Institutions
Team ID: LTVIP2025TMID42878

