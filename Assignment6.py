for a in range(0,10):
    score=input("please input score: ")
    if 60 <= score <= 100:
        if 60 <= score <= 69:
            print "your score is", score,";" , "Your Grade is D"
        if 70 <= score <= 79:
            print "your score is", score,";" , "Your Grade is C"
        if 80 <= score <= 89:
            print "your score is", score,";" , "Your Grade is B"
        if 90 <= score <= 100:
            print "your score is", score,";" , "Your Grade is B"
    else:
        print "please input a score between 60 and 100"
    print "end of the program! bye!"        
