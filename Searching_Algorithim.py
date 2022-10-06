
list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100] #13 variables - 12 max - 9-10

def Round(x):
    if (x % 1) >= 0.5:
       y = x - (x % 1) + 1
    elif (x % 1) < 0.5:
       y = x - (x % 1)
    return int(y)

def Finder(array, num):
    x = 1
    y = 0
    z = 0
    max = len(array)-1
    min = 0
    next = 0
    last = 0
    current = Round((max)/2)
    
#    if array[current] > num:
#        next = current+max/2
#    elif array[current] < num:
#        next = current+min/2
#    elif num == array[current]:
#        print("Number ", num, "was found at position: ", current)
#        return True
#    elif current == last:
#        print("Number could not be found")
#        return False
#    next = Round(next)
#    last = current
#    current = next-1

    while x > 0:

        if num == array[current]:
            print("Number ", num, "was found at position: ", current)
            return True
        if current-last == 1 or current-last == -1:
            z = z - 1       
        if current == last or z == -2:
            print("Number could not be found")
            return False


        if array[current] < num and array[current] < last:
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
        
        
        
Finder(list, 88)
