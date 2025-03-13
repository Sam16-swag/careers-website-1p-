from flask import Flask,render_template
from flask_sqlalchemy import  SQLAlchemy
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_DATABASE_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_kjey=True)

@app.route("/")
def hello():
    return "hello"
@app.route('/stareter')
def stareter():
    return render_template('todo.html')

if __name__=="__main__":
    app.run(debug=True)