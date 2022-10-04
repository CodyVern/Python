test = [15, 8, 100, 36, 1]

def Sorter(Nums):
    lengh = len(Nums)-1
    x = 1                               #Set to initialize while loop
    while x > 0:
        x = 0                           #Loop will now stop unless defined otherwise
        for i in range(len(Nums)):
            temp = 0                    #empty var to swap integers
            if i < lengh:               #if i is > length during below's if, it'll error out
                if Nums[i] > Nums[i+1]: #Number unsorted in list 
                    x = 1               #Loop will now re-iterate through list
                    temp = Nums[i+1]
                    Nums[i+1] = Nums[i]
                    Nums[i] = temp
                    print(Nums[i+1], "Swapped with", Nums[i])

Sorter(test)

print(test)