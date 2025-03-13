from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/about')
def sam():
    name="sammy"
    return render_template('about.html',name2=name)

@app.route('/bootstrap')
def sammy():
    return render_template('bootstrap.html')

@app.route('/bootstrap2')
def sammy2():
    return render_template('bootstrap2.html')

if __name__ == '__main__':
    app.run(debug=True,port=8000)
