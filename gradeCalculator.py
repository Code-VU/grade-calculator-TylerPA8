def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you
    try:
        score = float(input("Enter score:"))
    except:
        score = 1.1
        #changes score when it finds error. Will throw bad score in following if statement.
    if score > 1 or score < 0:
        print("Bad score")
    elif score >= 0.9:
        print ("A")
    elif score >= 0.8:
        print ("B")
    elif score >= 0.7:
        print ("C")
    elif score >= 0.6:
        print ("D")
    else:
        print ("F")

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculateGrade()