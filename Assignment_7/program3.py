
#?              Python Programming Assignment based on Lambda functions
#! Accept a list of numbers from the user and use the filter() method to keep only even numbers.

#* Expected Input :
#* Enter a list : 1 2 3 4 5 6

#* Expected Output :
#* Even numbers : [ 2, 4, 6]


def main():
    print("Enter a list :")
    Data = list()

    for i in range(6):
        no = int(input())
        Data.append(no)
    
    filterData = list(filter(lambda x: x % 2 == 0, Data))
    print("Even numbers :", filterData)

if __name__ == "__main__":
    main()


# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity