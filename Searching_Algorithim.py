
from pickle import FALSE, TRUE


list = [1, 8, 15, 24, 36, 84, 95, 99, 100]

def Round(x):
    if (x % 1) >= 0.5:
       y = x - (x % 1) + 1
    elif (x % 1) < 0.5:
       y = x - (x % 1)
    return int(y)

def Finder(array, num):
    x = 1
    y = 0
    z = True
    max = len(array)-1
    min = 0
    next = 0
    last = 0
    current = Round((max)/2)
    
    while x > 0:

        if num == array[current]:
            print("Number ", num, "was found at position: ", current)
            return True
        if current == last:
            print("Number could not be found")
            return False

        if z == False:
            if array[current] > num and array[current] > last:
                next = current+max/2
            if array[current] > num and array[current] < last:
                next = current+last/2
            if array[current] < num and array[current] < last:
                next = current+min/2
            if array[current] < num and array[current] > last:
                next = current+last/2

        if z == True:
            if array[current] > num:
                next = current+max/2
            if array[current] < num:
                next = current+min/2
            z = False


        next = Round(next)
        last = current
        current = next
        y = y + 1
        print(y, ") current:", current, "| last:", last, "| next:", next)
        
        
        


Finder(list, 15)
