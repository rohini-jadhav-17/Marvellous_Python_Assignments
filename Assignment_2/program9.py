
#! Write a program which accept one number from user and return number of digits in that number.

#Input  :   5187934      Output :   7

def CountDigits(iNo):
    count = 0
    while(iNo != 0):
        iNo = int(iNo / 10)
        count += 1
    
    return count    

def main():
    print("Enter number :")
    iValue = int(input())

    iRet = CountDigits(iValue)
    print("The number of digits in number", iValue, "is :", iRet)

# Starter function
if __name__ == "__main__":
    main()