
#! Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.

#Input  :   Number of elements : 7
#Input Elements : 13    5   45  7   4   56  34     Output :  56

def MaxInList(Data):
    iMax = Data[0]
    for iNo in Data:
        if(iNo > iMax):
            iMax = iNo
    
    return iMax    

def main():
    print("Enter number of elements :")
    size = int(input())

    Data = list()

    print("Enter the values: ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    iRet = MaxInList(Data)
    print("The Maximum of all elements in list", Data, "is :", iRet)

# Starter function
if __name__ == "__main__":
    main()

# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity