
#! Write a program which contains filter(), map(), reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.

# Input List :  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]  
# List after filter : [2, 4, 4, 2, 8, 10]
# List after map : [4, 16, 16, 4, 64, 100]
# Output of reduce : 204

from functools import reduce

def main():
    print("Enter the number of elements :")
    size = int(input())

    Data = list()

    print("Enter numbers :")
    for i in range(size):
        no = int(input())
        Data.append(no)

    filterData = list(filter(lambda x: (x % 2 == 0), Data))
    print("Filter Data :", filterData)

    mapData = list(map(lambda x: (x ** 2), filterData))
    print("Map Data :", mapData)
    
    reduceData = reduce(lambda x, y: (x + y), mapData)
    print("Reduced Data :", reduceData)

# Starter function
if __name__ == "__main__":
    main()

# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity