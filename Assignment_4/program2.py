
#! Write a program which contains one lambda function which accepts two parameters and return its multiplication.

# Input  :  4  3     Output :  12
# Input  :  6  3     Output :  18

Multiply =  lambda x, y : x * y

def main():
    print("Enter first number :")
    iValue1 = int(input())

    print("Enter second number :")
    iValue2 = int(input())

    iRet = Multiply(iValue1, iValue2)
    print("Multiplication of", iValue1, "and", iValue2, "is :", iValue1, "*", iValue2, "=", iRet)

# Starter function
if __name__ == "__main__":
    main()

# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity