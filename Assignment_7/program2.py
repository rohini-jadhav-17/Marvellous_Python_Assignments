
#?              Python Programming Assignment based on Lambda functions
#! Accept a list of integers from the user and use the map() function to double each value.

#* Expected Input :
#* Enter a list : 1 2 3 4 5

#* Expected Output :
#* Doubled list : [ 2, 4, 6, 8, 10]


def main():
    print("Enter a list :")
    Data = list()

    for i in range(5):
        no = int(input())
        Data.append(no)
    
    mapData = list(map(lambda x: x * 2, Data))
    print("Doubled list :", mapData)

if __name__ == "__main__":
    main()


# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity