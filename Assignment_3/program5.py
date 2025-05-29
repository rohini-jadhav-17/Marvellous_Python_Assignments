
#! Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().

# Input  :   Number of elements : 11
# Input Elements : 13    5   45  7  4    56  10 34  2   5   8
# Output :  32 (13 + 5 + 7 + 2 + 5)

import MarvellousNum

def ListPrime(Data):
    iSum = 0
    primeData = list()
    for iNo in Data:
        if(MarvellousNum.ChkPrime(iNo)):
            iSum = iSum + iNo
            primeData.append(iNo)
    return iSum, primeData   

def main():
    print("Enter number of elements :")
    size = int(input())

    Data = list()

    print("Enter the values: ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    iRet, primeList = ListPrime(Data)
    print("The addition of all prime numbers in List", Data, "is :", iRet,"--->", primeList)

# Starter function
if __name__ == "__main__":
    main()

# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity