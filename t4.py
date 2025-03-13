from flask import Flask, request, render_template

app = Flask(__name__)  # Initialize Flask app

@app.route('/')
def index():
    return render_template('form.html')  # Render HTML form

@app.route('/submit', methods=['POST'])  # Handle form submission
def submit():
    name = request.form.get('name')  # Get "name" from form
    age = request.form.get('age')  # Get "age" from form
    return f"Received: Name - {name}, Age - {age}"  # Return response

if __name__ == '__main__':
    app.run(debug=True)  # Run the app
