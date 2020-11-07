#== MAIN FLASK APPLICATION ==#


#== MODULES ==#

#Flask Module - Used to create the website and allow for all of the intended features
from flask import Flask, render_template, url_for, request
#Random Module - Used to generate random numbers
from random import randint
#OS Module - Used to check if a file path exists
from os import path
#Time Module - Used to measure the time taken for an algorithm to complete
import time


#== SEARCHING AND SORTING FUNCTIONS ==#

#VALIDATION
#List Validation Function - Used to check that each item in a list is an integer
def validate(lst):
    valid = True
#Loops through the list checking that each item is a number
    for item in lst:
        try:
            int(item)
        except:
            valid = False
    return valid

#Order Validation Function
def inOrder(lst):
    order = True
#Loops through the list, checking if each item is lower than the next item
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            order = False
    return order

#BUBBLE SORT
#Bubble Sort Function - Used to sort a list in ascending order, using bubble sort
def bubbleSort(lst):
#Each item in the list converted into an integer
    lst = [int(x) for x in lst]
#Variable used to determine the number of comparisons made
    comps = 0
#Passes variable used to indicate when the list is sorted
    passes = -1
#Loopnum variable used to determine the number of comparisons needed in each loop
    loopnum = len(lst)-1
#Loop used to sort each item
    while loopnum > 0 and passes != 0:
        passes = 0
        for i in range(loopnum):
            comps += 1
#Loops through the list comparing each set of numbers.
            if lst[i] > lst[i+1]:
                passes += 1
                lst[i], lst[i+1] = lst[i+1], lst[i]
#Each loop, the last item is sorted, so loopnum can be decreased by one
        loopnum -= 1
    return lst, comps

#Reverse Bubble Sort Function - Used to sort a list in descending order, using bubble sort
#Same as bubbleSort()
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

#MERGE SORT
#Merge Function - Used to merge two ascending sorted lists into one ascending sorted list
def merge(lstA, lstB):
    comb = []
#Loops while both input lists still contain values
    while lstA and lstB:
#Each loop the first item in each list is compared, and the smaller of the two is removed from its respected list, and added to the return list
        if lstA[0] > lstB[0]:
            comb.append(lstB.pop(0))
        else:
            comb.append(lstA.pop(0))
#Returns the newly sorted list in addition to any remaining items
    return comb + lstA + lstB

#Merge Sort Function - Used to sort a list into ascending order using merge sort
def mergeSort(lst):
#If the list initially contains one or less items, the list is returned with 0 as the comparison count
    if len(lst) <= 1:
        return lst, 0
    else:
#Comps variable used to determine the number of comparisons
        comps = 0
#Takes the middle index of the list
        midIndex = len(lst) // 2
#Uses recursion to apply the mergeSort() function to the left side of the list
        left, cmps = mergeSort(lst[:midIndex])
#Uses recursion to apply the mergeSort() function to the right side of the list
        right, cmps2 = mergeSort(lst[midIndex:])
#Merges the two sorted lists, using the merge() function
        merged = merge(left, right)
        comps += cmps + cmps2 + 1
    return merged, comps

#Reverse Merge Sort Function - Used to merge two descending sorted lists into one descending sorted list
#Same as merge()
def mergeRev(lstA, lstB):
    comb = []
    while lstA and lstB:
        if lstA[0] < lstB[0]:
            comb.append(lstB.pop(0))
        else:
            comb.append(lstA.pop(0))
    return comb + lstA + lstB

#Reverse Merge Sort Function - Used to sort a list into descending order using merge sort
#Same as mergeSort()
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

#LINEAR SEARCH
#Linear Search Function - Used to check if an item is in a list by using linear search
def linearSearch(lst, searchItem):
#Converts each item in the list into an integer
    lst = [int(num) for num in lst]
#found variable used to determine if the item is within the list
    found = False
#comps variable used to determine the number of comparisons made
    comps = 0
#Count variable to determine the index value where the item is found
    count = 0
#Checks if each item in the list is the search item
    while not found and count < len(lst):
        comps += 1
        if lst[count] == searchItem:
            found = True
            return found, comps, count
        count += 1
    return found, comps, count

#BINARY SEARCH
#Binary Search Function - Used to check if an item is in a list by using binary search
def binarySearch(lst, min, max, searchItem):
#comps variable used to determine the number of comparisons made
    comps = 0
#Checks if the top index passed is larger than the bottom index passed.
    if min <= max:
#Takes the midpoint of the list
        midPoint = (min + max) // 2
        comps += 1
#If the search item is the midpoint, the function ends
        if lst[midPoint] == searchItem:
            return True, midPoint, comps
        elif lst[midPoint] > searchItem:
#Recursion is used to call the binarySearch() function on the lower half of the list if the search Item is below the midpoint
            srt, ind, cmps =  binarySearch(lst, min, midPoint-1, searchItem)
            comps += cmps
            return srt, ind, comps
        else:
#Recursion is used to call the binarySearch() function on the upper half of the list if the search Item is above the midpoint
            srt, ind, cmps = binarySearch(lst, midPoint+1, max, searchItem)
            comps += cmps
            return srt, ind, comps
#If the item is not found, false is returned
    else:
        return False, -1, comps


#== FLASK APP INITIALIZATION ==#

app = Flask(__name__)


#== APP CONSTANTS ==#

#Folder Path - Used to store input files in a single location
FOLDER = path.join(app.root_path, "uploads")


#== APP SETUP ==#

#HOME PAGE
#App route set so that when you first open the website, you will be taken to the home page
@app.route('/')
#Flask Home Function
def home():
#Returns the home html page
    return render_template("index.html")

#BUBBLE SORT ENTER PAGE
#App route set to /bubble/enter
#Post/Get allows the function to interact with the html page
@app.route('/bubble/enter', methods=['POST', 'GET'])
#Flask Bubble Sort Enter Function
def bubbleenter():
#Checks if the html page is posting to the function
    if request.method == 'POST':
#Sets the nums variable to user input
        nums = request.form['numbers']
#Sets the dir variable to user input
        dir = request.form['updown']
#Checks if the user has input anything
        if nums:
#Converts the input into a list (Input should be comma seperated)
            lst = nums.split(",")
#Removes any additional items (non-numbers) from the end of the list
            while lst[-1] in [",", ""]:
                lst.pop(-1)
#Validates that the list consists of numbers only using the validate() function
            if validate(lst):
#Converts each item in the list into an integer
                for i in range(len(lst)):
                    lst[i] = int(lst[i])
#Checks if the user wants to sort the list in ascending or descending order
                if str(dir) == "Ascending":
#Uses the time module to take the start and end time for the function to run
                    strt = time.time()
#Calls the bubble sort function on the list
                    srt, cmps = bubbleSort(lst)
                    end = time.time()
                else:
                    strt = time.time()
                    srt, cmps = bubbleSortRev(lst)
                    end = time.time()
#Determines the amount of time taken for the function to run
                tkn = end-strt
                if str(tkn) == "0.0":
#If the time is returned as 0.0, a suitable message is displayed
                    tkn = "Negligible"
#Returns the bubble enter html template with the necessary components added
                return render_template("bubbleenter.html", sorted = srt, unsorted = lst, compars = cmps, time = tkn)
            else:
#If the input is not valid, a suitable message is returned
                return render_template("bubbleenter.html", sorted = [], unsorted = ['Invalid List - List Format CSN'])
        else:
            return render_template("bubbleenter.html", sorted = [], unsorted = [])
    else:
        return render_template("bubbleenter.html", sorted = [], unsorted = [])

#BUBBLE SORT GENERATE PAGE
#App route set to /bubble/generate
#Post/Get allows the function to interact with the html page
@app.route('/bubble/generate', methods=['POST', 'GET'])
def bubblegnerate():
#Checks if anything is being posted from the html page
    if request.method == 'POST':
#amount variable set to user input
        amount = request.form['amount']
#rnge variable set to user input
        rnge = request.form['range']
#dir variable set to user input
        dir = request.form['updown']
#Checks if the user has input all necessary fields
        if amount and rnge:
#Uses try and except to validate user inputs
            try:
#Converts the num varibale into an integer
                num = int(amount)
                rnge = rnge.split(",")
#Converts the two numbers in the rnge variable into integers
                min = int(rnge[0])
                max = int(rnge[1])
                if len(rnge) == 2 and validate(rnge) and min < max:
#Sets the limits for the number of random numbers to a reasonable range
                    if num > 0 and num < 10001:
                        lst = []
#Generates a list of random numbers (range input) of length number input
                        for i in range(num):
                            lst.append(randint(min, max))
#Checks if the user wants to input the list in ascending or descending order
                        if str(dir) == "Ascending":
#Uses the time module to determine the start and end time of the function
                            strt = time.time()
#Calls the bubbleSort() function to sort the list
                            srt, cmps = bubbleSort(lst)
                            end = time.time()
                        else:
                            strt = time.time()
                            srt, cmps = bubbleSortRev(lst)
                            end = time.time()
#Calculates the amount of time it took for the function to run
                        tkn = end-strt
#If the time is returned as 0.0, an appropriate message is displayed
                        if str(tkn) == "0.0":
                            tkn = "Negligible"
#Returns the bubble generate template with all of the necessary components for display
                        return render_template("bubblegenerate.html", sort = srt, genlst = lst, compars = cmps, time = tkn)
#If an error is raised at any point throughout the function, and appropriate display is returned
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

#BUBBLE SORT FILE PAGE
#App route set to /bubble/file
#Post/Get allows the function to interact with the html page
@app.route('/bubble/file', methods=['POST', 'GET'])
def bubblefile():
#Checks if the html page is trying to post anything to the function
    if request.method == 'POST':
#Sets the filecont variable to user input
        filecont = request.files['theFile']
#Sets the dir varibale to user input
        dir = request.form['updown']
#Checks that the user has input the necessary variables
        if filecont:
#Sets the new filepath using the FOLDER constant variable
            newPath = path.join(FOLDER, filecont.filename)
#Splits the list so the filetype can be validated
            type = filecont.filename.split(".")
            if type[-1] == "csv":
#Checks if the file has been accessed before
                if not path.exists(newPath):
#If not the file is saved to the new location
                    filecont.save(newPath)
#The file is then opened to be read from
                with open(newPath, 'r') as file:
#Replaces all of the newline characters with empty characters
                    data = file.read().replace('\n', '')
                data = data.split(",")
#Validates the data in the file using the validate() function
                if validate(data):
#Converts each item in the list into an integer
                    for i in range(len(data)):
                        data[i] = int(data[i])
#Checks if the user wants to sort the list in ascending or descnedning order
                    if str(dir) == "Ascending":
#Uses the time module to check the start and end time of the function
                        strt = time.time()
#Sorts the list using the bubbleSort() function
                        srt, cmps = bubbleSort(data)
                        end = time.time()
                    else:
                        strt = time.time()
                        srt, cmps = bubbleSortRev(data)
                        end = time.time()
#Calculates the time taken
                    tkn = end-strt
#If the time is returned as 0.0, a suitable message is displayed
                    if str(tkn) == "0.0":
                        tkn = "Negligible"
#The bubblefile html template is returned with all of the necessary components
                    return render_template("bubblefile.html", cont=data, sort=srt, compars=cmps, time=tkn)
#If an error is raised at any point in the function, the bubblefile template is returned with an appropriate error message
                else:
                    return render_template("bubblefile.html", cont=['Invalid Path'], sort = [])
            else:
                return render_template("bubblefile.html", cont=['File must be .csv'], sort = [])
    return render_template("bubblefile.html", cont=[], sort = [])

#BUBBLE SORT EXPLANATION PAGE
#App route set to /bubble/explan
@app.route('/bubble/explan')
def bubbleexplan():
#No input is taken on this page, so the bubbleexpl html template is returned immediately
    return render_template("bubbleexpl.html")

#BUBBLE SORT COMPLEXITIES PAGE
#App route set to /bubble/comps
@app.route('/bubble/comps')
def bubblecomps():
#No input is taken on this page, so the bubblecomps html template is returned immediately
    return render_template("bubblecomps.html")

#Merge SORT ENTER PAGE
#App route set to /merge/enter
#Post/Get allows the function to interact with the html page
@app.route('/merge/enter', methods=['POST', 'GET'])
def mergeenter():
#Checks if anything is being posted from the html page to the function
    if request.method == 'POST':
#Nums variable set to user input
        nums = request.form['numbers']
#Dir variable set to user input
        dir = request.form['updown']
#Checks if the required forms have been input
        if nums:
            lst = nums.split(",")
#Removes any additional commas from the end of the list
            while lst[-1] in [",", ""]:
                lst.pop(-1)
#Validates the list using the validate() function
            if validate(lst):
#Converts each item in the list into an integer
                for i in range(len(lst)):
                    lst[i] = int(lst[i])
#Checks if the user wants to sort the list in ascending or descending order
                if str(dir) == "Ascending":
#Uses the time module to take the start and end time of the function
                    strt = time.time()
#Calls the mergeSort() function on the list
                    srt, cmp = mergeSort(lst)
                    end = time.time()
                else:
                    strt = time.time()
                    srt, cmp = mergeSortRev(lst)
                    end = time.time()
#Calculates the amount of time taken for the function to run
                tkn = end-strt
#If the result is returned as 0.0, an appropriate message is returned
                if str(tkn) == "0.0":
                    tkn = "Negligible"
#The html template is returned along with the necessary components for display
                return render_template("mergeenter.html", sorted = srt, unsorted = lst, time = tkn, compars = cmp)
#If any error is raised in the function, an approriate message is returned with the html template
            else:
                return render_template("mergeenter.html", sorted = [], unsorted = ['Invalid List - List Format CSN'])
        else:
            return render_template("mergeenter.html", sorted = [], unsorted = [])
    else:
        return render_template("mergeenter.html", sorted = [], unsorted = [])

#MERGE SORT GENERATE PAGE
#App route set to /merge/generate
#Post/Get allows the function to interact with the html page
@app.route('/merge/generate', methods=['POST', 'GET'])
def mergegnerate():
#Checks if anything is being posted to the function from the html page
    if request.method == 'POST':
#Amount variable set to user input
        amount = request.form['amount']
#rnge variable set to user input
        rnge = request.form['range']
#dir variable set to user input
        dir = request.form['updown']
#Checks that all necessary variables are present
        if amount and rnge:
#Uses a try except to validate the values as they are used
            try:
#Converts the num input into an integer
                num = int(amount)
                rnge = rnge.split(",")
#Converts the range values into integers
                min = int(rnge[0])
                max = int(rnge[1])
                if len(rnge) == 2 and validate(rnge) and min < max:
#Checks that the number of items being generated is within a reasonable range
                    if num > 0 and num < 10001:
                        lst = []
#Generates the list of random numbers
                        for i in range(num):
                            lst.append(randint(min, max))
#Checks if the user wants to sort in ascending or descending order
                        if str(dir) == "Ascending":
#Uses the time module to take the start and end time of the function
                            strt = time.time()
#Calls the mergeSort() function
                            srt, cmps = mergeSort(lst)
                            end = time.time()
                        else:
                            strt = time.time()
                            srt, cmps = mergeSortRev(lst)
                            end = time.time()
#Calculates the time taken for the function to run
                        tkn = end-strt
#If the time taken is returned as 0.0, an appropriate message is displayed
                        if str(tkn) == "0.0":
                            tkn = "Negligible"
#Returns the html template along with the necessary components for correct display
                        return render_template("mergegenerate.html", sort = srt, genlst = lst, compars = cmps, time = tkn)
#If any errors are raised throughout the function, the template is returned with an appropriate message to display
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

#MERGE SORT FILE PAGE
#App route set to /merge/file
#Post/Get allows the function to interact with the html page
@app.route('/merge/file', methods=['POST', 'GET'])
def mergeefile():
#Checks if anything is being posted to the function from the html file
    if request.method == 'POST':
#Sets the filecont variable to user input
        filecont = request.files['theFile']
#Sets the dir variable to user input
        dir = request.form['updown']
#Checks that everything required has been input
        if filecont and dir:
#Sets the filepath for the new file
            newPath = path.join(FOLDER, filecont.filename)
#Splits the list in order to validate the file type
            type = filecont.filename.split(".")
            if type[-1] == "csv":
#Checks if the file has been used before, if not, the file is added to the uploads folder
                if not path.exists(newPath):
                    filecont.save(newPath)
#Reads the file's content and converts it into list form
                with open(newPath, 'r') as file:
                    data = file.read().replace('\n', '')
                data = data.split(",")
#Validates the data using the validate() function
                if validate(data):
#Converts each item in the list into an integer
                    for i in range(len(data)):
                        data[i] = int(data[i])
#Checks if the user wants to sort the list in ascending or descending order
                    if str(dir) == "Ascending":
#Uses the time module to take the start and end time of the function
                        strt = time.time()
#Calls the mergeSort() function on the list
                        srt, cmps = mergeSort(data)
                        end = time.time()
                    else:
                        strt = time.time()
                        srt, cmps = mergeSortRev(data)
                        end = time.time()
#Calculates the amount of time take for the function to run
                    tkn = end-strt
#If tkn is returned as 0.0, a suitable message is displayed
                    if str(tkn) == "0.0":
                        tkn = "Negligible"
#The html template is returned along with the necessary display components
                    return render_template("mergeefile.html", cont=data, sort=srt, compars=cmps, time=tkn)
#If an error is raised at any point through the function, the html template is returned with an appropriate message
                else:
                    return render_template("mergeefile.html", cont=['Invalid Path'], sort = [])
            else:
                return render_template("mergeefile.html", cont=['File must be .csv'], sort = [])
    return render_template("mergeefile.html", cont=[], sort = [])


#MERGE SORT EXPLANATION PAGE
#App route set to /merge/explan
@app.route('/merge/explan')
def mergeexplan():
#No input is taken on this page, so the mergeexpl html template is returned immediately
    return render_template("mergeexpl.html")

#MERGE SORT EXPLANATION PAGE
#App route set to /merge/comps
@app.route('/merge/comps')
def mergecomps():
#No input is taken on this page, so the mergecomps html template is returned immediately
    return render_template("mergecomps.html")

#LINEAR SEARCH ENTER PAGE
#App route set to /linear/enter
#Post/Get allows the function to interact with the html page
@app.route('/linear/enter', methods=['POST', 'GET'])
def linearenter():
#Checks if anything is being posted to the function
    if request.method == 'POST':
#Sets the nums variable to user input
        nums = request.form['numbers']
#Sets the src variable to user input
        src = request.form['search']
#Checks that the required components have been input
        if nums and src:
            lst = nums.split(",")
#Removes any additional commas from the end of the input
            while lst[-1] in [",", ""]:
                lst.pop(-1)
#Validates the list using the validate() function
            if validate(lst) and validate(src):
#Converts each item in the list into an integer
                for i in range(len(lst)):
                    lst[i] = int(lst[i])
#Uses the time module to determine the start and end time of the function
                strt = time.time()
#Calls the linearSearch() function on the list and input search item
                srt, cmps, ind = linearSearch(lst, int(src))
                end = time.time()
#Calculates the time taken for the function to run
                tkn = end-strt
#If the time taken is returned as 0.0, an appropriate message is returned
                if str(tkn) == "0.0":
                    tkn = "Negligible"
#Returns the html template along with the necessary components for display
                if srt:
                    return render_template("linearenter.html", found = srt, searchItem = str(src), index = ind, genlst = lst, compars = cmps, time = tkn)
                else:
                    return render_template("linearenter.html", found = srt, searchItem = str(src), index = "-", genlst = lst, compars = cmps, time = tkn)
#If there are any errors raised through the function, the html template is returned with an appropriate error message
            else:
                return render_template("linearenter.html", genlst = ['Invalid List - List Format CSN'])
        else:
            return render_template("linearenter.html", genlst = [])
    else:
        return render_template("linearenter.html", genlst = [])

#LINEAR SEARCH GENERATE PAGE
#App route set to /linear/generate
#Post/Get allows the function to interact with the html page
@app.route('/linear/generate', methods=['POST', 'GET'])
def lineargenerate():
#Checks if anything is being posted to the function
    if request.method == 'POST':
#Amount variable set to user input
        amount = request.form['amount']
#Rnge varibale set to user input
        rnge = request.form['range']
#Checks if the correct variables have been input
        if amount and rnge:
#Try except used to validate the variables as they are used
            try:
#Converts the num variable to an integer
                num = int(amount)
                rnge = rnge.split(",")
#Converts the range variables into integers
                min = int(rnge[0])
                max = int(rnge[1])
#Converts the search item into an integer
                src = randint(min, max)
                if len(rnge) == 2 and min < max:
#Validates that the number of randome numbers being generated is within a reasonable range
                    if num > 0 and num < 10001:
                        lst = []
#Generates the list of random numbers
                        for i in range(num):
                            lst.append(randint(min, max))
#Uses the time module to determine the start and end time of the function
                        strt = time.time()
#Calls the linearSearch() function in order to preform the linear search
                        srt, cmps, ind = linearSearch(lst, src)
                        end = time.time()
#Calculates the time taken
                        tkn = end-strt
#If the time taken is returned as 0.0, an appropriate message is returned
                        if str(tkn) == "0.0":
                            tkn = "Negligible"
#Returns the html template with the necessary components for display
                        if srt:
                            return render_template("lineargen.html", found = srt, searchItem = str(src), index = ind, genlst = lst, compars = cmps, time = tkn)
                        else:
                            return render_template("lineargen.html", found = srt, searchItem = str(src), index = "-", genlst = lst, compars = cmps, time = tkn)
#If any errors are raised during the function, then the template is returned with an appropriate message
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

#LINEAR SEARCH FILE PAGE
#App route set to /linear/file
#Post/Get allows the function to interact with the html page
@app.route('/linear/file', methods=['POST', 'GET'])
def linearfile():
#Checks if anything is being posted to the function
    if request.method == 'POST':
#filecont variable set to user input
        filecont = request.files['theFile']
#src variable set to user input
        src = request.form['search']
#Checks that the necessary variables have been input
        if filecont and src:
#Uses try except to determine if the search item is an integer
            try:
                src = int(src)
            except:
                return render_template("linearfile.html", cont=['Search Item must be a number'], sort = [])
#Sets the filepath for the input file
            newPath = path.join(FOLDER, filecont.filename)
#Splits the filepath to validate file type
            type = filecont.filename.split(".")
            if type[-1] == "csv":
#If the path has not been accessed before, it is added to the uploads folder
                if not path.exists(newPath):
                    filecont.save(newPath)
#The file is opened to be read from
                with open(newPath, 'r') as file:
#Newline characters removed
                    data = file.read().replace('\n', '')
                data = data.split(",")
#Read list and search item validated using the validate() function
                if validate(data) and validate(src):
                    for i in range(len(data)):
                        data[i] = int(data[i])
#Time module used to determine the start and end time of the function
                    strt = time.time()
#linearSearch() function called
                    srt, cmps, ind = linearSearch(data, src)
                    end = time.time()
#Time taken is calculated
                    tkn = end-strt
#If the returned time is 0.0, an appropriate message is displayed
                    if str(tkn) == "0.0":
                        tkn = "Negligible"
#Returns the html template with the necessary components for display
                    if srt:
                        return render_template("linearfile.html", found = srt, searchItem = str(src), index = ind, genlst = data, compars = cmps, time = tkn)
                    else:
                        return render_template("linearfile.html", found = srt, searchItem = str(src), index = "-", genlst = data, compars = cmps, time = tkn)
#If an error is raised at any point in the function, the template is returned with an appropriate message
                else:
                    return render_template("linearfile.html", genlst = ['Invalid Content - Must be CSN'])
            else:
                return render_template("linearfile.html", genlst = ['File must be .csv'])
    return render_template("linearfile.html", genlst = [])

#LINEAR SEARCH EXPLANATION PAGE
#App route set to /linear/explan
@app.route('/linear/explan')
def linearexplan():
#No input is taken on this page, so the linearexpl html template is returned immediately
    return render_template("linearexpl.html")

#LINEAR SEARCH COMPLEXITIES PAGE
#App route set to /linear/comps
@app.route('/linear/comps')
def linearcomps():
#No input is taken on this page, so the linearcomps html template is returned immediately
    return render_template("linearcomps.html")

#BINARY SEARCH ENTER PAGE
#App route set to /binary/enter
#Post/Get allows the function to interact with the html page
@app.route('/binary/enter', methods=['POST', 'GET'])
def binaryenter():
#Checks if anything is being posted to the function
    if request.method == 'POST':
#Sets the nums variable to user input
        nums = request.form['numbers']
#Sets the src variable to user input
        src = request.form['search']
#Checks that the required variables have been input
        if nums and src:
            lst = nums.split(",")
#Removes any extra commas from the end of the list
            while lst[-1] in [",", ""]:
                lst.pop(-1)
#Validates the list and search item using the validate() function
            if validate(lst) and validate(src):
#Converts each item in the list into an integer
                for i in range(len(lst)):
                    lst[i] = int(lst[i])
#Checks that the list is in order by using the inOrder() function
                if inOrder(lst):
#Uses the time module to take the start and end time of the function
                    strt = time.time()
#Calls the binary search function
                    srt, ind, cmps = binarySearch(lst, 0, len(lst)-1, int(src))
                    end = time.time()
#Calculates the time taken for the function to run
                    tkn = end-strt
#If the time is returned as 0.0, an appropriate message is displayed
                    if str(tkn) == "0.0":
                        tkn = "Negligible"
#The html template is returned along with the necessary display components
                    if srt:
                        return render_template("binaryenter.html", found = srt, searchItem = str(src), index = ind, genlst = lst, compars = cmps, time = tkn)
                    else:
                        return render_template("binaryenter.htmll", found = srt, searchItem = str(src), index = "-", genlst = lst, compars = cmps, time = tkn)
#If an error is raised at any point throughout the function, the template is returned along with an appropriate error message
                else:
                    return render_template("binaryenter.html", genlst = ['Invalid List - Must be Sorted'])
            else:
                return render_template("binaryenter.html", genlst = ['Invalid List - List Format CSN'])
        else:
            return render_template("binaryenter.html", genlst = [])
    else:
        return render_template("binaryenter.html", genlst = [])

#BINARY SEARCH GENERATE PAGE
#App route set to /binary/generate
#Post/Get allows the function to interact with the html page
@app.route('/binary/generate', methods=['POST', 'GET'])
def binarygenerate():
#Checks if anything is being posted to the function from the html page
    if request.method == 'POST':
#Sets the amount variable to user input
        amount = request.form['amount']
#Sets the rnge variable to user input
        rnge = request.form['range']
#Checks that the correct variables have been entered
        if amount and rnge:
#Try except is used to validate all of the variables as the program is run
            try:
#num is converted into an integer
                num = int(amount)
                rnge = rnge.split(",")
#range variables are converted into integers
                min = int(rnge[0])
                max = int(rnge[1])
#random search item is generated
                src = randint(min, max)
                if len(rnge) == 2 and min < max:
#The number of random numbers being generated is validated (Ensures that it is within a reasonable range)
                    if num > 0 and num < 10001:
                        lst = []
#Generates the random list
                        for i in range(num):
                            lst.append(randint(min, max))
#Sorts the list so binary search can be applied
                        lst = mergeSort(lst)[0]
#Time module is used to take the start and end time of the function
                        strt = time.time()
#binarySearch() function is called on the lst and src
                        srt, ind, cmps = binarySearch(lst, 0, len(lst)-1, int(src))
                        end = time.time()
#The time taken for the function to run is calculated
                        tkn = end-strt
#If the time is returned as 0.0, an appropriate message is displayed.
                        if str(tkn) == "0.0":
                            tkn = "Negligible"
#The html template is returned along with all necessary components for display
                        if srt:
                            return render_template("binarygen.html", found = srt, searchItem = str(src), index = ind, genlst = lst, compars = cmps, time = tkn)
                        else:
                            return render_template("binarygen.html", found = srt, searchItem = str(src), index = "-", genlst = lst, compars = cmps, time = tkn)
#If any errors are raised throughout the function, the html template is returned with an appropriate message
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

#BINARY SEARCH FILE PAGE
#App route set to /binary/file
#Post/Get allows the function to interact with the html page
@app.route('/binary/file', methods=['POST', 'GET'])
def binaryfile():
#Checks if anything is being posted from the html page to the function
    if request.method == 'POST':
#filecont variable set to user input
        filecont = request.files['theFile']
#src variable set to user input
        src = request.form['search']
#Checks that the required variables are entered
        if filecont and src:
#Try except is used to validate the input search item
            try:
                src = int(src)
            except:
                return render_template("linearfile.html", cont=['Search Item must be a number'], sort = [])
#The filepath is set for the new file
            newPath = path.join(FOLDER, filecont.filename)
#The filepath is split in order for the file type to be validated
            type = filecont.filename.split(".")
            if type[-1] == "csv":
#If the file has not been accessed before, it is added to the uploads folder
                if not path.exists(newPath):
                    filecont.save(newPath)
#The file is read and content saved to a variable
                with open(newPath, 'r') as file:
                    data = file.read().replace('\n', '')
                data = data.split(",")
#The data and search item are validated
                if validate(data) and validate(src):
#Each item in the list is converted into an integer
                    for i in range(len(data)):
                        data[i] = int(data[i])
#Checks if the list is in order using the inOrder() function
                    if inOrder(data):
#The time module is used to determine the start and end times of the function
                        strt = time.time()
#The binarySearch() function is called on the data and search item
                        srt, ind, cmps = binarySearch(data, 0, len(data)-1, src)
                        end = time.time()
#The time taken for the function to run is calculated
                        tkn = end-strt
#If the time taken is returned as 0.0, an appropriate message is returned
                        if str(tkn) == "0.0":
                            tkn = "Negligible"
#The html template is returned along with the appropriate display components
                        if srt:
                            return render_template("binaryfile.html", found = srt, searchItem = str(src), index = ind, genlst = data, compars = cmps, time = tkn)
                        else:
                            return render_template("binaryfile.html", found = srt, searchItem = str(src), index = "-", genlst = data, compars = cmps, time = tkn)
#If an error is raised at any point throughout the function, the html template is returned with an appropriate message
                    else:
                        return render_template("binaryfile.html", genlst=['Invalid Content - Must be sorted'])
                else:
                    return render_template("binaryfile.html", genlst=['Invalid Content - Must be CSN'])
            else:
                return render_template("binaryfile.html", genlst=['File must be .csv'])
    return render_template("binaryfile.html", genlst=[])

#BINARY SEARCH EXPLANATION PAGE
#App route set to /binary/explan
@app.route('/binary/explan')
def binaryexplan():
#No input is taken on this page, so the binaryexpl html template is returned immediately
    return render_template("binaryexpl.html")

#BINARY SEARCH COMPLEXITIES PAGE
#App route set to /binary/comps
@app.route('/binary/comps')
def binarycomps():
#No input is taken on this page, so the binarycomps html template is returned immediately
    return render_template("binarycomps.html")
