from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

app = Flask(__name__)
model = load_model('final_waste_classifier - Copy (5).h5')

@app.route('/', methods=['GET', 'POST'])
def index():
    file_path = session.get('file_path', None)
    prediction_label = None

    if request.method == 'POST':
        action = request.form.get('action', None)
        
        if 'file' not in request.files:
            return jsonify({'status': 'error', 'message': 'No file part'})

        file = request.files['file']

        if file.filename == '':
            return jsonify({'status': 'error', 'message': 'No selected file'})

        if action == "Upload" or not action:  # Handle both direct upload and asynchronous upload
            # Save the uploaded file temporarily
            file_path = "static/uploads/" + file.filename
            file.save(file_path)
            session['file_path'] = file_path
            
            image_url = url_for('static', filename='uploads/' + os.path.basename(file_path))
            return jsonify({'status': 'success', 'image_url': image_url})

        elif action == "Classify" and file_path and os.path.exists(file_path):
            # Load the image using the saved path
            image = load_img(file_path, target_size=(150, 150))
            image = img_to_array(image)
            image = np.expand_dims(image, axis=0)
            prediction = model.predict(image)
            confidence = prediction if prediction >= 0.5 else (1 - prediction)

            if prediction >= 0.5:
                prediction_label = 'Recyclable'
            else:
                prediction_label = 'Organic'
            
            return jsonify({'status': 'success', 'prediction': prediction_label})

    return render_template('index.html')

if __name__ == "__main__":
    app.secret_key = 'some_secret_key'  # for session
    app.run(debug=True)
