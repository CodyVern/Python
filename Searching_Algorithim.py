
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
    max = len(array)
    min = 0
    next = 0
    last = 0
    current = Round((max)/2)
    
    if array[current] > num:
        next = current+max/2
    elif array[current] < num:
        next = current+min/2
    elif num == array[current]:
        print("Number ", num, "was found at position: ", current)
        return True
    elif current == last:
        print("Number could not be found")
        return False


    while x > 0:

        if num == array[current]:
            print("Number ", num, "was found at position: ", current)
            return True
        elif current == last:
            print("Number could not be found")
            return False

        elif array[current] < num and array[current] < last:
                next = current+max/2
        elif array[current] < num and array[current] > last:
                next = current+last/2
        elif array[current] > num and array[current] > last:
                next = current+min/2
        elif array[current] > num and array[current] < last:
                next = current+last/2

        next = Round(next)
        last = current
        current = next-1
        y = y + 1
        print(y, ") current:", current, "| last:", last)
        
        
        


Finder(list, 99)
