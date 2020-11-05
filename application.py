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

def merge(lstA, lstB):
    comb = []
    while lstA and lstB:
        if lstA[0] > lstB[0]:
            comb.append(lstB.pop(0))
        else:
            comb.append(lstA.pop(0))
    return comb + lstA + lstB

def mergeSort(lst):
    if len(lst) <= 1:
        return lst, 0
    else:
        comps = 0
        midIndex = len(lst) // 2
        left, cmps = mergeSort(lst[:midIndex])
        right, cmps2 = mergeSort(lst[midIndex:])
        merged = merge(left, right)
        comps += cmps + cmps2 + 1
    return merged, comps

def mergeRev(lstA, lstB):
    comb = []
    while lstA and lstB:
        if lstA[0] < lstB[0]:
            comb.append(lstB.pop(0))
        else:
            comb.append(lstA.pop(0))
    return comb + lstA + lstB

def mergeSortRev(lst):
    if len(lst) <= 1:
        return lst, 0
    else:
        comps = 0
        midIndex = len(lst) // 2
        left, cmps = mergeSortRev(lst[:midIndex])
        right, cmps2 = mergeSortRev(lst[midIndex:])
        merged = mergeRev(left, right)
        comps += cmps + cmps2 + 1
    return merged, comps

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

def binarySearch(lst, min, max, searchItem):
    comps = 0
    if min <= max:
        midPoint = (min + max) // 2
        comps += 1
        if lst[midPoint] == searchItem:
            return True, midPoint, comps
        elif lst[midPoint] > searchItem:
            srt, ind, cmps =  binarySearch(lst, min, midPoint-1, searchItem)
            comps += cmps
            return srt, ind, comps
        else:
            srt, ind, cmps = binarySearch(lst, midPoint+1, max, searchItem)
            comps += cmps
            return srt, ind, comps
    else:
        return False, -1, comps

def inOrder(lst):
    order = True
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            order = False
    return order

app = Flask(__name__)

FOLDER = path.join(app.root_path, "uploads")

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
        filecont = request.files['theFile']
        dir = request.form['updown']
        if filecont and dir:
            newPath = path.join(FOLDER, filecont.filename)
            dir = request.form['updown']
            type = filecont.filename.split(".")
            if type[-1] == "csv":
                if not path.exists(newPath):
                    filecont.save(newPath)
                with open(newPath, 'r') as file:
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
                    srt, cmp = mergeSort(lst)
                    end = time.time()
                else:
                    strt = time.time()
                    srt, cmp = mergeSortRev(lst)
                    end = time.time()
                tkn = end-strt
                if str(tkn) == "0.0":
                    tkn = "Negligible"
                return render_template("mergeenter.html", sorted = srt, unsorted = lst, time = tkn, compars = cmp)
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
        filecont = request.files['theFile']
        dir = request.form['updown']
        if filecont and dir:
            newPath = path.join(FOLDER, filecont.filename)
            type = filecont.filename.split(".")
            if type[-1] == "csv":
                if not path.exists(newPath):
                    filecont.save(newPath)
                with open(newPath, 'r') as file:
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
                    return render_template("mergeefile.html", cont=data, sort=srt, compars=cmps, time=tkn)
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
                    return render_template("linearenter.html", found = srt, searchItem = str(src), index = ind, genlst = lst, compars = cmps, time = tkn)
                else:
                    return render_template("linearenter.html", found = srt, searchItem = str(src), index = "-", genlst = lst, compars = cmps, time = tkn)
            else:
                return render_template("linearenter.html", genlst = ['Invalid List - List Format CSN'])
        else:
            return render_template("linearenter.html", genlst = [])
    else:
        return render_template("linearenter.html", genlst = [])


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
        filecont = request.files['theFile']
        src = request.form['search']
        if filecont and src:
            try:
                src = int(src)
            except:
                return render_template("linearfile.html", cont=['Search Item must be a number'], sort = [])
            newPath = path.join(FOLDER, filecont.filename)
            type = filecont.filename.split(".")
            if type[-1] == "csv":
                if not path.exists(newPath):
                    filecont.save(newPath)
                with open(newPath, 'r') as file:
                    data = file.read().replace('\n', '')
                data = data.split(",")
                if validate(data):
                    for i in range(len(data)):
                        data[i] = int(data[i])
                    strt = time.time()
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
                    return render_template("linearfile.html", genlst = ['Invalid Content - Must be CSN'])
            else:
                return render_template("linearfile.html", genlst = ['File must be .csv'])
    return render_template("linearfile.html", genlst = [])

@app.route('/linear/explan')
def linearexplan():
    return render_template("linearexpl.html")


@app.route('/linear/comps')
def linearcomps():
    return render_template("linearcomps.html")


@app.route('/binary/enter', methods=['POST', 'GET'])
def binaryenter():
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
                if inOrder(lst):
                    strt = time.time()
                    srt, ind, cmps = binarySearch(lst, 0, len(lst)-1, int(src))
                    end = time.time()
                    tkn = end-strt
                    if str(tkn) == "0.0":
                        tkn = "Negligible"
                    if srt:
                        return render_template("binaryenter.html", found = srt, searchItem = str(src), index = ind, genlst = lst, compars = cmps, time = tkn)
                    else:
                        return render_template("binaryenter.htmll", found = srt, searchItem = str(src), index = "-", genlst = lst, compars = cmps, time = tkn)
                else:
                    return render_template("binaryenter.html", genlst = ['Invalid List - Must be Sorted'])
            else:
                return render_template("binaryenter.html", genlst = ['Invalid List - List Format CSN'])
        else:
            return render_template("binaryenter.html", genlst = [])
    else:
        return render_template("binaryenter.html", genlst = [])


@app.route('/binary/generate', methods=['POST', 'GET'])
def binarygenerate():
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
                        lst = mergeSort(lst)[0]
                        strt = time.time()
                        srt, ind, cmps = binarySearch(lst, 0, len(lst)-1, int(src))
                        end = time.time()
                        tkn = end-strt
                        if str(tkn) == "0.0":
                            tkn = "Negligible"
                        if srt:
                            return render_template("binarygen.html", found = srt, searchItem = str(src), index = ind, genlst = lst, compars = cmps, time = tkn)
                        else:
                            return render_template("binarygen.html", found = srt, searchItem = str(src), index = "-", genlst = lst, compars = cmps, time = tkn)
                    else:
                        return render_template("binarygen.html", genlst = ['Amount out of Range'])
                else:
                    return render_template("binarygen.html", genlst = ['Invalid Range - Format "min, max"'])
            except:
                return render_template("binarygen.html", genlst = ['Invalid Input - Amount Format "num" - Range Format "min, max"'])
        else:
                return render_template("binarygen.html", genlst = [])
    else:
        return render_template("binarygen.html", genlst = [])


@app.route('/binary/file', methods=['POST', 'GET'])
def binaryfile():
    if request.method == 'POST':
        filecont = request.files['theFile']
        src = request.form['search']
        if filecont and src:
            try:
                src = int(src)
            except:
                return render_template("linearfile.html", cont=['Search Item must be a number'], sort = [])
            newPath = path.join(FOLDER, filecont.filename)
            type = filecont.filename.split(".")
            if type[-1] == "csv":
                if not path.exists(newPath):
                    filecont.save(newPath)
                with open(newPath, 'r') as file:
                    data = file.read().replace('\n', '')
                data = data.split(",")
                if validate(data):
                    for i in range(len(data)):
                        data[i] = int(data[i])
                    if inOrder(data):
                        strt = time.time()
                        srt, ind, cmps = binarySearch(data, 0, len(data)-1, src)
                        end = time.time()
                        tkn = end-strt
                        if str(tkn) == "0.0":
                            tkn = "Negligible"
                        if srt:
                            return render_template("binaryfile.html", found = srt, searchItem = str(src), index = ind, genlst = data, compars = cmps, time = tkn)
                        else:
                            return render_template("binaryfile.html", found = srt, searchItem = str(src), index = "-", genlst = data, compars = cmps, time = tkn)
                    else:
                        return render_template("binaryfile.html", genlst=['Invalid Content - Must be sorted'])
                else:
                    return render_template("binaryfile.html", genlst=['Invalid Content - Must be CSN'])
            else:
                return render_template("binaryfile.html", genlst=['File must be .csv'])
    return render_template("binaryfile.html", genlst=[])

@app.route('/binary/explan')
def binaryexplan():
    return render_template("binaryexpl.html")


@app.route('/binary/comps')
def binarycomps():
    return render_template("binarycomps.html")
