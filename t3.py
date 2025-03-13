from flask import Flask, request
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        return "This a post request."
    return "This is a get request"
if __name__=="__main__":
    app.run(debug=True)
