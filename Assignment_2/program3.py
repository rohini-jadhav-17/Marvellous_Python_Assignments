
#! Write a program which accept one number from user and return its factorial

#Input  :   5
#Output :   120

def Factorial(iNo):
    fact = 1
    while(iNo != 0):
        fact = fact * iNo
        iNo -= 1
    return fact

def main():
    print("Enter number :")
    iValue = int(input())

    iRet = Factorial(iValue)
    print("Factorial of ", iValue, "is :", iRet)

# Starter function
if __name__ == "__main__":
    main()