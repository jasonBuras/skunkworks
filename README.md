# Request Form (Testing Grounds)
This project consists of a simple form submission setup using a Flask backend and an HTML frontend. Users can submit their name, email, message, and optionally attach an image. The form data is saved on the server side to a CSV file, and any uploaded images are stored in an `uploads` directory.

*This is a proof of concept*

# How does this work?
```
server.py receives POST requests containing form data, including
name, email, message, and an optional image file. It saves the image
(if provided) to the `uploads` folder and appends the form data to
a CSV file (`submissions.csv`).

```
```
Form Data:
- name (str): The user's name (required).
- email (str): The user's email address (required).
- message (str): The user's message (required).
- image (file): An optional image file uploaded by the user.
```

# How do I use it?
```
Run the Flask application on localhost at port 5000.

The server will start listening for requests at:
http://localhost:5000/submit

You can test this endpoint by sending a POST request with form data.
    
```

## Requirements

- Python 3.x
- Flask
- flask-cors (for handling cross-origin requests)

## Setup Instructions
Either clone this repo or download the files individually.

1. Install Flask and Flask-CORS
```bash
pip install Flask flask-cors
```
2. Download: [server.py](server/server.py)
3. Run server.py
```bash
python server.py:
```
4. Access the [Form Page](https://jasonburas.github.io/skunkworks/index.html)
	- This can also be done locally by downloading [index.html](docs/index.html) and opening it with a browser.
5. Fill out the form
	- Once you click submit, the directory the server is hosted in should create an uploads/ directory (for images), and a submissions.csv file (for the text fields).  

# Considerations/Notes
- The current build has no safeguards to check for valid emails.
- We need to talk to pod-9 about Authentication, and pod-4 about the database