list = []
temp = 0
indexing = 0
import random
for i in range(1,100):
    list.append(random.randint(0,10000))
# print list
for x in range(99,1,-1):
    # print x
    for y in range(0,x-1):
        # print y
        if list[y] > list[y+1]:
            temp = list[y]
            list[y] = list[y+1]
            list[y+1]=temp
print list
