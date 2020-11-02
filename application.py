from flask import Flask, render_template, url_for, request
from random import randint
from os import path
import time

def bubbleSort(lst):
    lst = [int(x) for x in lst]
    comps = 0
    passes = -1
    loopnum = len(lst)-1
    while loopnum > 0 and passes != 0:
        passes = 0
        for i in range(loopnum):
            comps += 1
            if lst[i] > lst[i+1]:
                passes += 1
                lst[i], lst[i+1] = lst[i+1], lst[i]
        loopnum -= 1
    return lst, comps

def bubbleSortRev(lst):
    lst = [int(x) for x in lst]
    comps = 0
    passes = -1
    loopnum = len(lst)-1
    while loopnum > 0 and passes != 0:
        passes = 0
        for i in range(loopnum):
            comps += 1
            if lst[i] < lst[i+1]:
                passes += 1
                lst[i], lst[i+1] = lst[i+1], lst[i]
        loopnum -= 1
    return lst, comps

def validate(lst):
    valid = True
    for item  in lst:
        try:
            int(item)
        except:
            valid = False
    return valid

def sort(lstA, lstB):
    returnLst = []
    comps = 0
    while lstA and lstB:
        comps += 1
        if lstA[0] < lstB[0]:
            returnLst.append(lstA.pop(0))
        else:
            returnLst.append(lstB.pop(0))
    return returnLst + lstA + lstB, comps

def mergeSort(lst):
    split = [[int(num)] for num in lst]
    comps = 0
    while len(split) != 1:
        i = 0
        while i < len(split)-1:
            sorted, adder = sort(split[i], split.pop(i+1))
            split[i] = sorted
            comps += adder
            i += 1
    return split[0], comps

def sortRev(lstA, lstB):
    returnLst = []
    comps = 0
    while lstA and lstB:
        comps += 1
        if lstA[0] > lstB[0]:
            returnLst.append(lstA.pop(0))
        else:
            returnLst.append(lstB.pop(0))
    return returnLst + lstA + lstB, comps

def mergeSortRev(lst):
    split = [[int(num)] for num in lst]
    comps = 0
    while len(split) != 1:
        i = 0
        while i < len(split)-1:
            sorted, adder = sortRev(split[i], split.pop(i+1))
            comps += adder
            split[i] = sorted
            i += 1
    return split[0], comps

def linearSearch(lst, searchItem):
    lst = [int(num) for num in lst]
    found = False
    comps = 0
    count = 0
    while not found and count < len(lst):
        comps += 1
        if lst[count] == searchItem:
            found = True
            return found, comps, count
        count += 1
    return found, comps, count



app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/bubble/enter', methods=['POST', 'GET'])
def bubbleenter():
    if request.method == 'POST':
        nums = request.form['numbers']
        dir = request.form['updown']
        if nums:
            lst = nums.split(",")
            while lst[-1] in [",", ""]:
                lst.pop(-1)
            if validate(lst):
                for i in range(len(lst)):
                    lst[i] = int(lst[i])
                if str(dir) == "Ascending":
                    strt = time.time()
                    srt, cmps = bubbleSort(lst)
                    end = time.time()
                else:
                    strt = time.time()
                    srt, cmps = bubbleSortRev(lst)
                    end = time.time()
                tkn = end-strt
                if str(tkn) == "0.0":
                    tkn = "Negligible"
                return render_template("bubbleenter.html", sorted = srt, unsorted = lst, compars = cmps, time = tkn)
            else:
                return render_template("bubbleenter.html", sorted = [], unsorted = ['Invalid List - List Format CSN'])
        else:
            return render_template("bubbleenter.html", sorted = [], unsorted = [])
    else:
        return render_template("bubbleenter.html", sorted = [], unsorted = [])


@app.route('/bubble/generate', methods=['POST', 'GET'])
def bubblegnerate():
    if request.method == 'POST':
        amount = request.form['amount']
        rnge = request.form['range']
        dir = request.form['updown']
        if amount and rnge:
            try:
                num = int(amount)
                rnge = rnge.split(",")
                min = int(rnge[0])
                max = int(rnge[1])
                if len(rnge) == 2 and validate(rnge) and min < max:
                    if num > 0 and num < 10001:
                        lst = []
                        for i in range(num):
                            lst.append(randint(min, max))
                        if str(dir) == "Ascending":
                            strt = time.time()
                            srt, cmps = bubbleSort(lst)
                            end = time.time()
                        else:
                            strt = time.time()
                            srt, cmps = bubbleSortRev(lst)
                            end = time.time()
                        tkn = end-strt
                        if str(tkn) == "0.0":
                            tkn = "Negligible"
                        return render_template("bubblegenerate.html", sort = srt, genlst = lst, compars = cmps, time = tkn)
                    else:
                        return render_template("bubblegenerate.html", sort = [], genlst = ['Amount out of Range'])
                else:
                    return render_template("bubblegenerate.html", sort = [], genlst = ['Invalid Range - Format "min, max"'])
            except:
                return render_template("bubblegenerate.html", sort = [], genlst = ['Invalid Input - Amount Format "num" - Range Format "min, max"'])
        else:
                return render_template("bubblegenerate.html", sort = [], genlst = [])
    else:
        return render_template("bubblegenerate.html", sort = [], genlst = [])


@app.route('/bubble/file', methods=['POST', 'GET'])
def bubblefile():
    if request.method == 'POST':
        filecont = request.form['filepath']
        dir = request.form['updown']
        type = filecont.split(".")
        if type[-1] == "csv":
            if path.exists(filecont):
                with open(filecont, 'r') as file:
                    data = file.read().replace('\n', '')
                data = data.split(",")
                if validate(data):
                    for i in range(len(data)):
                        data[i] = int(data[i])
                    if str(dir) == "Ascending":
                        strt = time.time()
                        srt, cmps = bubbleSort(data)
                        end = time.time()
                    else:
                        strt = time.time()
                        srt, cmps = bubbleSortRev(data)
                        end = time.time()
                    tkn = end-strt
                    if str(tkn) == "0.0":
                        tkn = "Negligible"
                    return render_template("bubblefile.html", cont=data, sort=srt, compars=cmps, time=tkn)
                else:
                    return render_template("bubblefile.html", cont=['Invalid Data'], sort = [])
            else:
                return render_template("bubblefile.html", cont=['Invalid Path'], sort = [])
        else:
            return render_template("bubblefile.html", cont=['File must be .csv'], sort = [])
    return render_template("bubblefile.html", cont=[], sort = [])

@app.route('/bubble/explan')
def bubbleexplan():
    return render_template("bubbleexpl.html")


@app.route('/bubble/comps')
def bubblecomps():
    return render_template("bubblecomps.html")


@app.route('/merge/enter', methods=['POST', 'GET'])
def mergeenter():
    if request.method == 'POST':
        nums = request.form['numbers']
        dir = request.form['updown']
        if nums:
            lst = nums.split(",")
            while lst[-1] in [",", ""]:
                lst.pop(-1)
            if validate(lst):
                for i in range(len(lst)):
                    lst[i] = int(lst[i])
                if str(dir) == "Ascending":
                    strt = time.time()
                    srt, cmps = mergeSort(lst)
                    end = time.time()
                else:
                    strt = time.time()
                    srt, cmps = mergeSortRev(lst)
                    end = time.time()
                tkn = end-strt
                if str(tkn) == "0.0":
                    tkn = "Negligible"
                return render_template("mergeenter.html", sorted = srt, unsorted = lst, compars = cmps, time = tkn)
            else:
                return render_template("mergeenter.html", sorted = [], unsorted = ['Invalid List - List Format CSN'])
        else:
            return render_template("mergeenter.html", sorted = [], unsorted = [])
    else:
        return render_template("mergeenter.html", sorted = [], unsorted = [])


@app.route('/merge/generate', methods=['POST', 'GET'])
def mergegnerate():
    if request.method == 'POST':
        amount = request.form['amount']
        rnge = request.form['range']
        dir = request.form['updown']
        if amount and rnge:
            try:
                num = int(amount)
                rnge = rnge.split(",")
                min = int(rnge[0])
                max = int(rnge[1])
                if len(rnge) == 2 and validate(rnge) and min < max:
                    if num > 0 and num < 10001:
                        lst = []
                        for i in range(num):
                            lst.append(randint(min, max))
                        if str(dir) == "Ascending":
                            strt = time.time()
                            srt, cmps = mergeSort(lst)
                            end = time.time()
                        else:
                            strt = time.time()
                            srt, cmps = mergeSortRev(lst)
                            end = time.time()
                        tkn = end-strt
                        if str(tkn) == "0.0":
                            tkn = "Negligible"
                        return render_template("mergegenerate.html", sort = srt, genlst = lst, compars = cmps, time = tkn)
                    else:
                        return render_template("mergegenerate.html", sort = [], genlst = ['Amount out of Range'])
                else:
                    return render_template("mergegenerate.html", sort = [], genlst = ['Invalid Range - Format "min, max"'])
            except:
                return render_template("mergegenerate.html", sort = [], genlst = ['Invalid Input - Amount Format "num" - Range Format "min, max"'])
        else:
                return render_template("mergegenerate.html", sort = [], genlst = [])
    else:
        return render_template("mergegenerate.html", sort = [], genlst = [])


@app.route('/merge/file', methods=['POST', 'GET'])
def mergeefile():
    if request.method == 'POST':
        filecont = request.form['filepath']
        dir = request.form['updown']
        if filecont:
            type = filecont.split(".")
        if filecont and type[-1] == "csv":
            if path.exists(filecont):
                with open(filecont, 'r') as file:
                    data = file.read().replace('\n', '')
                data = data.split(",")
                if validate(data):
                    for i in range(len(data)):
                        data[i] = int(data[i])
                    if str(dir) == "Ascending":
                        strt = time.time()
                        srt, cmps = mergeSort(data)
                        end = time.time()
                    else:
                        strt = time.time()
                        srt, cmps = mergeSortRev(data)
                        end = time.time()
                    tkn = end-strt
                    if str(tkn) == "0.0":
                        tkn = "Negligible"
                    return render_template("mergeefile.html", cont=data, sort=srt, compars = cmps, time = tkn)
                else:
                    return render_template("mergeefile.html", cont=['Invalid Data'], sort = [])
            else:
                return render_template("mergeefile.html", cont=['Invalid Path'], sort = [])
        else:
            return render_template("mergeefile.html", cont=['File must be .csv'], sort = [])
    return render_template("mergeefile.html", cont=[], sort = [])


@app.route('/merge/explan')
def mergeexplan():
    return render_template("mergeexpl.html")


@app.route('/merge/comps')
def mergecomps():
    return render_template("mergecomps.html")


@app.route('/linear/enter', methods=['POST', 'GET'])
def linearenter():
    if request.method == 'POST':
        nums = request.form['numbers']
        src = request.form['search']
        if nums and src:
            lst = nums.split(",")
            while lst[-1] in [",", ""]:
                lst.pop(-1)
            if validate(lst):
                for i in range(len(lst)):
                    lst[i] = int(lst[i])
                strt = time.time()
                srt, cmps, ind = linearSearch(lst, int(src))
                end = time.time()
                tkn = end-strt
                if str(tkn) == "0.0":
                    tkn = "Negligible"
                if srt:
                    return render_template("lineargen.html", found = srt, searchItem = str(src), index = ind, genlst = lst, compars = cmps, time = tkn)
                else:
                    return render_template("lineargen.html", found = srt, searchItem = str(src), index = "-", genlst = lst, compars = cmps, time = tkn)
            else:
                return render_template("linearenter.html", unsorted = ['Invalid List - List Format CSN'])
        else:
            return render_template("linearenter.html", unsorted = [])
    else:
        return render_template("linearenter.html", unsorted = [])


@app.route('/linear/generate', methods=['POST', 'GET'])
def lineargenerate():
    if request.method == 'POST':
        amount = request.form['amount']
        rnge = request.form['range']
        if amount and rnge:
            try:
                num = int(amount)
                rnge = rnge.split(",")
                min = int(rnge[0])
                max = int(rnge[1])
                src = randint(min, max)
                if len(rnge) == 2 and min < max:
                    if num > 0 and num < 10001:
                        lst = []
                        for i in range(num):
                            lst.append(randint(min, max))
                        strt = time.time()
                        srt, cmps, ind = linearSearch(lst, src)
                        end = time.time()
                        tkn = end-strt
                        if str(tkn) == "0.0":
                            tkn = "Negligible"
                        if srt:
                            return render_template("lineargen.html", found = srt, searchItem = str(src), index = ind, genlst = lst, compars = cmps, time = tkn)
                        else:
                            return render_template("lineargen.html", found = srt, searchItem = str(src), index = "-", genlst = lst, compars = cmps, time = tkn)
                    else:
                        return render_template("lineargen.html", genlst = ['Amount out of Range'])
                else:
                    return render_template("lineargen.html", genlst = ['Invalid Range - Format "min, max"'])
            except:
                return render_template("lineargen.html", genlst = ['Invalid Input - Amount Format "num" - Range Format "min, max"'])
        else:
                return render_template("lineargen.html", genlst = [])
    else:
        return render_template("lineargen.html", genlst = [])


@app.route('/linear/file', methods=['POST', 'GET'])
def linearfile():
    if request.method == 'POST':
        filecont = request.form['filepath']
        src = request.form['search']
        type = filecont.split(".")
        if type[-1] == "csv" and src:
            if path.exists(filecont):
                with open(filecont, 'r') as file:
                    data = file.read().replace('\n', '')
                data = data.split(",")
                if validate(data) and validate(src):
                    for i in range(len(data)):
                        data[i] = int(data[i])
                    strt = time.time()
                    src = int(src)
                    srt, cmps, ind = linearSearch(data, src)
                    end = time.time()
                    tkn = end-strt
                    if str(tkn) == "0.0":
                        tkn = "Negligible"
                    if srt:
                        return render_template("linearfile.html", found = srt, searchItem = str(src), index = ind, genlst = data, compars = cmps, time = tkn)
                    else:
                        return render_template("linearfile.html", found = srt, searchItem = str(src), index = "-", genlst = data, compars = cmps, time = tkn)
                else:
                    return render_template("linearfile.html", genlst=['Invalid Data'])
            else:
                return render_template("linearfile.html", genlst=['Invalid Path'])
        else:
            return render_template("linearfile.html", genlst=['File must be .csv'])
    return render_template("linearfile.html", genlst=[])

@app.route('/linear/explan')
def linearexplan():
    return render_template("linearexpl.html")


@app.route('/linear/comps')
def linearcomps():
    return render_template("linearcomps.html")
