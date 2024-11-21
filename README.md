# Request Form (Testing Grounds)
This project consists of a simple form submission setup using a Flask backend and an HTML frontend. Users can submit their name, email, message, and optionally attach an image. The form data is saved on the server side to a CSV file, and any uploaded images are stored in an `uploads` directory.

*This is a proof of concept.* 

Pod-4's implementation of SQLalchemy will replace the functionality of [server.py](server/server.py). It currently just serves as a tester for the request form.

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
3. Run server.py:
- Navigate to the directory server.py is in and run:
```bash
python server.py
```
or
```bash
py server.py
```
- Note that this will produce a Warning:
```bash
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
```
- This is a standard notification from Flask indicating that the built-in development server is not intended for production use. The development server is suitable for testing and development because it provides features like auto-reloading and detailed error messages, but it lacks the performance and security features needed for a production environment. 
4. Access the [Form Page](https://jasonburas.github.io/skunkworks/index.html)
	- Note: This can also be done locally by downloading [index.html](docs/index.html) and opening it with a browser application.
5. Fill out the form
	- Once you click submit, the directory the server is hosted in should create an uploads/ directory (for images), and a submissions.csv file (for the text fields).  

# Considerations/Notes
- Security
	- The current build has no safeguards to check for valid emails.
	- We need to talk to pod-9 about Authentication, and pod-4 about the database
	- May have to look into a way to limit file size
- Design
	- This is currently just a proof of concept. Now that we have established a foundation, we will spend some time focusing on the design. 