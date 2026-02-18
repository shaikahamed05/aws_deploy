from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def hello_world():
    return render_template("index.html")

# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9000)
