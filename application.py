from flask import Flask, render_template, url_for, request
from random import randint
from os import path

def bubbleSort(lst):
    lst = [int(x) for x in lst]
    lenlist = len(lst)
    for i in range(lenlist-1):
        for j in range(0, lenlist-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def validate(lst):
    valid = True
    for item  in lst:
        try:
            int(item)
        except:
            valid = False
    return valid

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/bubble/enter', methods=['POST', 'GET'])
def bubbleenter():
    if request.method == 'POST':
        task_content = request.form['numbers']
        if task_content:
            task_content = task_content.split(",")
            while task_content[-1] in [",", ""]:
                task_content.pop(-1)
            if validate(task_content):
                task_content = bubbleSort(task_content)
                return render_template("bubbleenter.html", sorted = task_content)
            else:
                return render_template("bubbleenter.html", sorted = [])
        else:
            return render_template("bubbleenter.html", sorted = [])
    else:
        return render_template("bubbleenter.html", sorted = [])


@app.route('/bubble/generate', methods=['POST', 'GET'])
def bubblegnerate():
    if request.method == 'POST':
        amount = request.form['amount']
        rnge = request.form['range']
        if amount and rnge:
            try:
                num = int(amount)
                rnge = rnge.split(",")
                min = int(rnge[0])
                max = int(rnge[1])
                if len(rnge) == 2 and validate(rnge) and min < max:
                    if num > 0 and num < 101:
                        lst = []
                        for i in range(num):
                            lst.append(randint(min, max))
                        srt = bubbleSort(lst)
                        return render_template("bubblegenerate.html", sort = srt, genlst = lst)
                    else:
                        return render_template("bubblegenerate.html", sort = [], genlst = ['Invalid Amount'])
                else:
                    return render_template("bubblegenerate.html", sort = [], genlst = ['Invalid Range'])
            except:
                return render_template("bubblegenerate.html", sort = [], genlst = ['Invalid Amount'])
        else:
                return render_template("bubblegenerate.html", sort = [], genlst = [])
    else:
        return render_template("bubblegenerate.html", sort = [], genlst = [])


@app.route('/bubble/file', methods=['POST', 'GET'])
def bubblefile():
    if request.method == 'POST':
        filecont = request.form['filepath']
        type = filecont.split(".")
        if type[-1] == "csv":
            if path.exists(filecont):
                with open(filecont, 'r') as file:
                    data = file.read().replace('\n', '')
                data = data.split(",")
                if validate(data):
                    for i in range(len(data)):
                        data[i] = int(data[i])
                    datasrt = bubbleSort(data)
                    return render_template("bubblefile.html", cont=data, sort=datasrt)
                else:
                    return render_template("bubblefile.html", cont=['Invalid Data'], sort = [])
            else:
                return render_template("bubblefile.html", cont=['Invalid Path'], sort = [])
        else:
            return render_template("bubblefile.html", cont=['File must be .csv'], sort = [])
    return render_template("bubblefile.html", cont=[], sort = [])
