from flask import Flask

app = Flask(__name__)

@app.route('/admin')
def admin():
    return "admin"

@app.route('/librarian')
def librarian():
    return "librarian"

@app.route('/student')
def student():
    return "student"

@app.route('/user/<name>')
def user(name):
    if name=='admin':
        return redirect(url_for('admin'))
    elif name=='librarian':
        return redirect(url_for('librarian'))
    elif name=='student':
        return redirect(url_for('student'))
    else :
        return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)
