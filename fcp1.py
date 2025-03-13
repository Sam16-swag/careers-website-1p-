from flask import Flask,render_template, jsonify

app = Flask(__name__)

JOBS=[
    {
        'id':1,
        'title':"Data Analyst",
        'location':"Banglore Inida",
        'salary':"Rs. 10,00,000"
    }
    ,{
        'id':2,
        'title':"Data Scientist",
        'location':"Delhi India",
        'salary':"Rs. 15,00,000"
    }
    ,{
        'id':3,
        'title':"Frontend Engineer",
        'location':"Remote",
    }
    ,{
        'id':4,
        'title':"Backend Engineer",
        'location':"San Francico USA",
        'salary':"$120,000"
    }
]

@app.route('/')
def hello():
    return render_template("j2.html",jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)
