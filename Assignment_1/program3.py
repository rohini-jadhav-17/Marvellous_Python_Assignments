
#! Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.

# Input :   11  5        Output :    16

def Add(iNo1, iNo2):
    iResult = iNo1 + iNo2
    return iResult

def main():
    print("Enter the first number :")
    iValue1 = int(input())

    print("Enter the second number :")
    iValue2 = int(input())

    iRet = Add(iValue1, iValue2)
    print("The addition is :", iRet)

# Starter function
if __name__ == "__main__":
    main()