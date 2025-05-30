
#?              Python Programming Assignment based on Lambda functions
#! Write a function that accepts a list of integers and returns a list of prime numbers using filter().

#* Expected Input :
#* Enter a list : 10 11 12 13 14 15 16 17

#* Expected Output :
#* Prime numbers : [11, 13, 17]

def Prime(iNo):
    stop = int(iNo / 2)
    bFlag = True
    for i in range(2, stop + 1):
        if(iNo % i == 0):
            bFlag = False
    
    return bFlag

def main():
    print("Enter a list :")
    Data = list()

    for i in range(8):
        no = int(input())
        Data.append(no)
    
    filterData = list(filter(Prime, Data))
    print("Prime numbers :", filterData)

if __name__ == "__main__":
    main()


# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity