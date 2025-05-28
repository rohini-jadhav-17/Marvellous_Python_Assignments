
#! Write a program which contains one function that accept one number from user and returns true if the number is divisible by 5 otherwise returns false.

#Input : 8     Output :   False
#Input : 25     Output :  True

def ChkDivByFive(iNo):
    if((iNo % 5) == 0):
        return True
    else:
        return False

def main():
    print("Enter number :")
    iValue = int(input())

    bRet = ChkDivByFive(iValue)
    if(bRet == True):
        print("The given number is divisible by 5")
    else:
        print("The given number is not divisible by 5")

# Starter function
if __name__ == "__main__":
    main()