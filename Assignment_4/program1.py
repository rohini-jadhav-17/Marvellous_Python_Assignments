
#! Write a program which contains one lambda function which accepts one parameter and return poower of two.

# Input  :  4       Output :  16
# Input  :  6       Output :  36

powerOfTwo =  lambda x : x**2

def main():
    print("Enter number :")
    iValue = int(input())

    iRet = powerOfTwo(iValue)
    print("Square of", iValue, "is :", iRet)

# Starter function
if __name__ == "__main__":
    main()

# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity