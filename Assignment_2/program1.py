
#! create one module named as Arithmetic which contains four functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. Write one python program which call all the functions from Arithmetic module by accepting the parameters from user.

import Arithmetic

def main():
    print("Enter first number :")
    iValue1 = int(input())

    print("Enter second number :")
    iValue2 = int(input())

    add = Arithmetic.Add(iValue1, iValue2)
    print("Addition is :", add)

    sub = Arithmetic.Sub(iValue1, iValue2)
    print("Subtraction is :", sub)

    mult = Arithmetic.Mult(iValue1, iValue2)
    print("Multiplication is :", mult)

    div = Arithmetic.Div(iValue1, iValue2)
    print("Division is :", div)

# Starter function
if __name__ == "__main__":
    main()