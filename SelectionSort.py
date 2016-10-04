# sorting 100 random numbers took 0.115s
# sorting 10000 random numbers took 15.969s
# sorting by moving the min value to the left ONLY
def randomList(length):
    import random
    list=[]
    for i in range(0, length):
        list.append(random.randint(0, 100))
    return list


list=randomList(10)
print "original list", [62, 22, 64, 51, 10, 48, 36, 4, 41, 59]


def selectionSort(list):
    for x in range(0, len(list)/2):
        min = list[x]
        min_index = x
        max = list[x]
        max_index = x
        for y in range(x+1,len(list)-x):
            if list[y]< min :
                min = list[y]
                min_index = y

            if list[y]> max :
                max = list[y]
                max_index = y
        endpos=len(list)-x-1
        print list, x, min_index, len(list)-x-1, max_index
        if (min_index == len(list)-x-1 and max_index == x):
            (list[min_index],list[x])=(list[x], list[min_index])
        elif (max_index == x):
            (list[max_index], list[endpos]) = (list[endpos], list[max_index])
            (list[x], list[min_index]) = (list[min_index], list[x])
        else:
            (list[min_index],list[x])=(list[x], list[min_index])
            (list[max_index],list[endpos])=(list[endpos], list[max_index])
    print "sorted list : ", list
    return list
selectionSort([62, 22, 64, 51, 10, 48, 36, 4, 41, 59])
