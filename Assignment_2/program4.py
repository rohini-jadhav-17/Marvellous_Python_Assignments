
#! Write a program which accept one number from user and return addition of its factors.

#Input  :   12
#Output :   16    (1+2+3+4+6)

def Factors(iNo):
    stop = int(iNo / 2)
    iSum = 0
    for i in range(1, stop + 1):
        if((iNo % i) == 0):
            iSum = iSum + i
    
    return iSum

def main():
    print("Enter number :")
    iValue = int(input())

    iRet = Factors(iValue)
    print("Addition of factors of number", iValue, "is :", iRet)

# Starter function
if __name__ == "__main__":
    main()