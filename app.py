from flask import Flask, render_template, url_for, redirect,request

## Create the flask app

app = Flask(__name__)

@app.route('/')
def home():
    return "Home page"

@app.route('/welcome')
def welcome():
    return "Welcome to flask tuturial"

@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method == 'GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        
        
        avg_marks = (maths+science+history)/3
        
        result = ""
        if avg_marks>=50:
            result = "success"
        else:
            result="fail"
        return render_template("calculate.html",results=avg_marks, abc=result,maths=maths, science=science, history=history )

if __name__=='__main__':
    app.run(debug=True)