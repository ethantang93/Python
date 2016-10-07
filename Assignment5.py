def multiply(a, x):
    for i in range(0,len(a)):
        a[i] = a[i] * x
    return a
a=[1,2,3,4,5]
b = multiply(a,2)
print b
