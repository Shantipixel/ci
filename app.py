from flask import Flask
from math_utils import add, subtract

app=Flask(__name__)
@app.route('/')
def home():
    return "CI CD app is running"
@app.route('/add/<int:a>/<int:b>')
def add_numbers(a,b):
    result= add(a,b)
    return f"{a} + {b} = {result}"
@app.route('/subtract/<int:a>/<int:b>')
def subtract_numbers(a,b):
    result=subtract(a,b)
    return f"{a}-{b}={result}"
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)