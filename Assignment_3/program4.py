
#! Write a program which accept N numbers from user and store it into List. Accept one another number from user and return the frequency of that number from List.

# Input  :   Number of elements : 11
# Input Elements : 13    5   45  7  4    56  5   34  2   5   65
# Element to search :  5      
# Output :  3

def SearchInList(Data, searchNo):
    count = 0
    for iNo in Data:
        if(iNo == searchNo):
            count += 1
    
    return count    

def main():
    print("Enter number of elements :")
    size = int(input())

    Data = list()

    print("Enter the values: ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Enter the element to search : ")
    searchElem = int(input())

    iRet = SearchInList(Data, searchElem)
    print(searchElem, "occurs", iRet, "times in List :", Data)

# Starter function
if __name__ == "__main__":
    main()

# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity