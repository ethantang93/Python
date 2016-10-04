def randomList(length):
    import random
    list=[]
    for i in range(0, length):
        list.append(random.randint(0, 100))
    return list

list = randomList(10)
print list
def insertionSort(list):
    for x in range(1,len(list)):
        currentvalue = list[x]
        position = x
        while position>0 and list[position-1]>currentvalue:
            list[position] = list[position-1]
            position = position-1
        list[position]=currentvalue
    print list
insertionSort(list)
