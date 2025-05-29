
#! Write a program which contains filter(), map(), reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

# Input List :  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]  
# List after filter : [76, 89, 86, 90, 70]
# List after map : [86, 99, 96, 100, 80]
# Output of reduce : 6538752000

from functools import reduce

def main():
    print("Enter the number of elements :")
    size = int(input())

    Data = list()

    print("Enter numbers :")
    for i in range(size):
        no = int(input())
        Data.append(no)

    filterData = list(filter(lambda x: (x >= 70) and (x <= 90), Data))
    print("Filter Data :", filterData)

    mapData = list(map(lambda x: (x + 10), filterData))
    print("Map Data :", mapData)
    
    reduceData = reduce(lambda x, y: (x * y), mapData)
    print("Reduced Data :", reduceData)

# Starter function
if __name__ == "__main__":
    main()

# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity