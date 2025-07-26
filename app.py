import os
import numpy as np
import cv2
import base64
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename
app = Flask(__name__)
# Load your trained model
model = load_model("Blood Cell.keras")  # Ensure this matches your actual model filename
# Update this list to match your actual training dataset
class_labels = ['monocyte', 'neutrophil','eosinophil', 'lymphocyte']  # Adjust if needed
def predict_image_class(image_path, model):
    img = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_resized = cv2.resize(img_gray, (28, 28))
    img_normalized = img_resized.astype('float32') / 255.0
    img_flattened = img_normalized.flatten()
    input_tensor = np.expand_dims(img_flattened, axis=0)  # shape: (1, 784)

    predictions = model.predict(input_tensor)
    predicted_class_idx = np.argmax(predictions, axis=1)[0]

    print("🧠 Raw Predictions:", predictions)
    print("🔢 Predicted index:", predicted_class_idx)

    if predicted_class_idx >= len(class_labels):
        predicted_class_label = "Unknown"
    else:
        predicted_class_label = class_labels[predicted_class_idx]

    return predicted_class_label, cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            upload_dir = os.path.join(os.getcwd(), 'uploads')
            os.makedirs(upload_dir, exist_ok=True)
            file_path = os.path.join(upload_dir, secure_filename(file.filename))
            file.save(file_path)
            class_label, img = predict_image_class(file_path, model)
            if img is not None:
                _, buffer = cv2.imencode('.jpg', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
                img_data = base64.b64encode(buffer).decode('utf-8')
            else:
                img_data = None
            return render_template('result.html', class_label=class_label, img_data=img_data)
    return render_template("home.html")
if __name__ == "__main__":
    app.run(debug=True)