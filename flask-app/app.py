# Import the Flask class from the Flask library
from flask import Flask

 # Create an instance of the Flask application
app = Flask(__name__)


# Define a route for the root URL ("/")
@app.route("/")
def main():   # Define a function that will execute when the root URL is accessed
    return "Hi there from Python Flask application.\n"  # Return a simple string response to the client.


# Start the Flask app on all available network interfaces (0.0.0.0) and port 8080
app.run(host='0.0.0.0', port=8080)