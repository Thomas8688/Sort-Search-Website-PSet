from flask import Flask, render_template, url_for, request

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
    if valid:
        return True
    else:
        return False

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", sorted = "HOMEPAGE")


@app.route('/bubble', methods=['POST', 'GET'])
def bubble():
    if request.method == 'POST':
        task_content = request.form['numbers']
        task_content = task_content.split(",")
        while task_content[-1] in [",", ""]:
            task_content.pop(-1)
        if validate(task_content):
            task_content = bubbleSort(task_content)
            return render_template("bubble.html", sorted = task_content)
        else:
            return render_template("bubble.html", sorted = ['Invalid Input'])
    else:
        return render_template("bubble.html", sorted = [])
