# Web development frameworks are available with Python

from flask import Flask # Install Flask if it is not available
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to SiriSarah LLC!"

# Run only when it is run as main program
if __name__ == "__main__":
    app.run()

# Once the program starts, navigate to http://127.0.0.1:5000 on your browser to see the results.
# To learn more, https://flask.palletsprojects.com/en/2.1.x/