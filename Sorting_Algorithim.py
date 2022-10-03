test = [12, 4, 3, 2, 8]

def Sorter(Nums):
    lengh = len(Nums)-1
    x = 1
    while x > 0:
        x = 0
        for i in range(len(Nums)):
            temp = 0
            if i < lengh:
                if Nums[i] > Nums[i+1]:
                    x = 1
                    temp = Nums[i+1]
                    Nums[i+1] = Nums[i]
                    Nums[i] = temp
                    print(Nums[i], "Swapped with", Nums[i+1])
            

Sorter(test)

print(test)