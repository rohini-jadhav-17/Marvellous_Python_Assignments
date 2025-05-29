
#! Write a program which contains filter(), map(), reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers (You can also use normal functions instead of lambda functions)

# Input List :  [2, 70, 11, 10, 17, 23, 31, 77]  
# List after filter : [2, 11, 17, 23, 31]
# List after map : [4, 22, 34, 46, 62]
# Output of reduce : 62

from functools import reduce

def filterFun(iNo):
    stop = int(iNo / 2)
    bFlag = True
    for i in range(2, stop + 1):
        if(iNo % i == 0):
            bFlag = False
    
    return bFlag

def multiplyByTwo(iNo):
    return iNo * 2

def maxInList(iNo1, iNo2):
    iMax = iNo1
    if(iNo2 > iMax):
        iMax = iNo2
    
    return iMax

def main():
    print("Enter the number of elements :")
    size = int(input())

    Data = list()

    print("Enter numbers :")
    for i in range(size):
        no = int(input())
        Data.append(no)

    filterData = list(filter(filterFun, Data))
    print("Filter Data :", filterData)

    mapData = list(map(multiplyByTwo, filterData))
    print("Map Data :", mapData)
    
    reduceData = reduce(maxInList, mapData)
    print("Reduced Data :", reduceData)

# Starter function
if __name__ == "__main__":
    main()

# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity