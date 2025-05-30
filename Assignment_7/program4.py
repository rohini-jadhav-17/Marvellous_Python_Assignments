
#?              Python Programming Assignment based on Lambda functions
#! Accept a list of numbers from the user and use reduce() method (from functools) to find the product of all numbers.

#* Expected Input :
#* Enter a list : 2 3 4

#* Expected Output :
#* Product : 24

from functools import reduce

def main():
    print("Enter a list :")
    Data = list()

    for i in range(3):
        no = int(input())
        Data.append(no)
    
    reduceData = reduce(lambda x, y: x * y , Data)
    print("Product :", reduceData)

if __name__ == "__main__":
    main()


# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity