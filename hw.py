from flask import Flask

# Create a Flask web service
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the web service
if __name__ == '__main__':
    app.run()