from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi"

@app.route('/home/name/<name>')  # Changed URL
def hello(name):
    return "Hello " + name

@app.route('/home/age/<int:age>')  # Changed URL
def show_age(age):
    return f"Age = {age}"

@app.route('/home/<any(foo,baa,za):identifier>')  # Changed URL
def item(identifier,value):
    return f"Item with identifier:{identifier}"

def show_user(username):
    return f"Hello {username} !"

app.add_url_rule('/user/<username>', 'show_user', show_user) 

if __name__ == '__main__':
    app.run(debug=True)
