
#! Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

#Input  :   Number of elements : 6
#Input Elements : 13    5   45  7   4   56      Output :  130

def SumInList(Data):
    iSum = 0
    for iNo in Data:
        iSum = iSum + iNo
    
    return iSum    

def main():
    print("Enter number of elements :")
    size = int(input())

    Data = list()

    print("Enter the values: ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    iRet = SumInList(Data)
    print("The addition of all elements in list", Data, "is :", iRet)

# Starter function
if __name__ == "__main__":
    main()

# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity