
#! Write a program which accept one number from user and return addition of digits in that number.

#Input  :   5187934      Output :   37

def SumDigits(iNo):
    iSum = 0
    iDigit = 0
    while(iNo != 0):
        iDigit = int(iNo % 10)
        iNo = int(iNo / 10)
        iSum += iDigit
    
    return iSum    

def main():
    print("Enter number :")
    iValue = int(input())

    iRet = SumDigits(iValue)
    print("The number of digits in number", iValue, "is :", iRet)

# Starter function
if __name__ == "__main__":
    main()