
#! Write a program which accept one number from user and check whether number is prime or not.

#Input  :   5
#Output :   It is Prime Number

def CheckPrime(iNo):
    stop = int(iNo / 2)
    bFlag = True
    for i in range(2, stop + 1):
        if((iNo % i) == 0):
            bFlag = False
            break
    
    return bFlag

def main():
    print("Enter number :")
    iValue = int(input())

    bRet = CheckPrime(iValue)

    if(bRet == True):
        print(iValue, "is Prime Number")
    else:
        print(iValue, "is Not Prime Number")

# Starter function
if __name__ == "__main__":
    main()