from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/merge')
def Merge():
    return 'Merge Sort'

@app.route('/bubble')
def Bubble():
    return 'Bubble Sort'

@app.route('/linear')
def Linear():
    return 'Linear Search'

@app.route('/binary')
def Binary():
    return 'Binary Search'
