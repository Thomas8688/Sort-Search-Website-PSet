from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/MergeSort')
def Merge():
    return 'Merge Sort'

@app.route('/BubbleSort')
def Bubble():
    return 'Bubble Sort'

@app.route('/LinearSearch')
def Linear():
    return 'Linear Search'

@app.route('/BinarySearch')
def Binary():
    return 'Binary Search'
