
list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100] #13 variables - 12 max - 9-10

def Round(x):
    if (x % 1) >= 0.5:
       y = x - (x % 1) + 1
    elif (x % 1) < 0.5:
       y = x - (x % 1)
    return int(y)

def Finder(array, num):
    max = len(array)
    min = 0
    mid = Round(max/2)
    x = False

    while x == False:
        if array[mid-1] == num:
            print("Number: ", num, " Found at position: ", mid)
            return True
        elif array[max-1] == array[mid-1]:
            print("Number not found")
            return False
        elif array[mid-1] > num:
            max = mid
            mid = Round((mid+min)/2)
        elif array[mid-1] < num:
            min = mid
            mid = Round((mid+max)/2)
        print("mid: ", mid, "| max: ", max, " | min: ", min)
        
        
Finder(list, 88)
