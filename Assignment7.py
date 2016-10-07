import random
heads=0
tails=0
toss=0
for i in range(0,5001):
    toss=random.random()
    toss=round(toss)
    if toss == 0 :
        heads +=1
        print "Attempt #%d: Throwing a coin... It's a head! ... Got %d head(s) so far and %d tail(s) so far " %(i, heads, tails)
    if toss == 1 :
        tails +=1
        print "Attempt #%d: Throwing a coin... It's a tail! ... Got %d head(s) so far and %d tail(s) so far " %(i, heads, tails)
print 'ending the program! thank you!'
