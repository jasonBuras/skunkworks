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

# Define the CSV file for storing submissions
CSV_FILE = 'submissions.csv'

# Ensure the CSV file has headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Add headers
        writer.writerow(['Name', 'Email', 'Message', 'Image Path', 'Start Date', 'End Date', 'Tags'])

@app.route('/submit', methods=['POST'])
def submit_form():
    """
    This is for testing purposes. 
    Pod-4, feel free to use this and convert this function to work with sqllite

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
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        tags = request.form.getlist('tags')  # Retrieve tags as a list
        images = request.files.getlist('images')  # Retrieve multiple uploaded files

        if not name or not email or not message or not start_date or not end_date or not tags:
            # Return a JSON response with an error if any required field is missing (should be handled in the form, but swiss cheese model)
            return jsonify({'error': 'Missing required fields'}), 400

        # Save the image if it exists
        image_paths = []
        if images:
            for image in images:
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                image.save(image_path)
                image_paths.append(image_path)

        # Append the data to a CSV file
        with open('submissions.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                name, 
                email, 
                message, 
                ";".join(image_paths),  # Save image paths as a semicolon-separated string
                start_date, 
                end_date, 
                ",".join(tags)
            ])

        # Return a JSON response with submitted data
        return jsonify({
            'message': 'Form submitted successfully',
            'data': {
                'name': name,
                'email': email,
                'message': message,
                'start_date': start_date,
                'end_date': end_date,
                'tags': tags,
                'image_paths': image_paths
            }
        })
    except Exception as e:
        print("Error processing form:", e)
        # Return a JSON response with an error message
        return jsonify({'error': 'Server error'}), 500

if __name__ == '__main__':
    """
    Run the Flask application on localhost at port 5000.
    """
    app.run(host='localhost', port=5000)