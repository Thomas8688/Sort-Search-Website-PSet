from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
    #return 'Home Page'

@app.route('/merge')
def Merge():
    return render_template("merge.html")

@app.route('/bubble')
def Bubble():
    return render_template("bubble.html")

@app.route('/linear')
def Linear():
    return render_template("linear.html")

@app.route('/binary')
def Binary():
    return render_template("binary.html")
