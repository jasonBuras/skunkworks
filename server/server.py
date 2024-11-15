import csv
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the uploads directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/submit', methods=['POST'])
def submit_form():
    """
    This is for testing purposes. 
    Pod-4, feel free to use this and convert this function to work with sqlalchemy

    Handles form submission at the `/submit` endpoint.

    This endpoint receives POST requests containing form data, including
    name, email, message, and an optional image file. It saves the image
    (if provided) to the `uploads` folder and appends the form data to
    a CSV file (`submissions.csv`).

    Form Data:
        - name (str): The user's name (required).
        - email (str): The user's email address (required).
        - message (str): The user's message (required).
        - image (file): An optional image file uploaded by the user.

    Returns:
        JSON: A response with a success message and the submitted form data,
              or an error message if the submission failed.

    Raises:
        400 Bad Request: If required fields (name, email, message) are missing.
        500 Server Error: If there is an error processing the form submission.
    """
    try:
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        image = request.files.get('image')

        if not name or not email or not message:
            # Return a JSON response with an error if any required field is missing (should be handled in the form, but swiss cheese model)
            return jsonify({'error': 'Missing required fields'}), 400

        # Save the image if it exists
        image_path = None
        if image:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)

        # Append the data to a CSV file
        with open('submissions.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, message, image_path])

        # Return a JSON response with submitted data
        return jsonify({
            'message': 'Form submitted successfully',
            'name': name,
            'email': email,
            'user_message': message
        })
    except Exception as e:
        print("Error processing form:", e)
        # Return a JSON response with an error message
        return jsonify({'error': 'Server error'}), 500

if __name__ == '__main__':
    """
    Run the Flask application on localhost at port 5000.

    The server will start listening for requests at:
    http://localhost:5000/submit

    You can test this endpoint by sending a POST request with form data.
    """
    app.run(host='localhost', port=5000)