def oddOccuring(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res

arr = []

n = int(input("enter array size: "))

while(n):
    num = int(input("enter number: "))
    arr.append(num)
    n-=1
