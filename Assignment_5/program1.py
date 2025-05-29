
#?              Python Programming Assignment based on data types on conditional logic
#! Arithmetic operations on Two Numbers
#! Write a program to accept two integers from the user and display their:
#! * Sum
#! * Difference
#! * Product
#! * Division

#* Expected Input : 
#* Enter first number: 10
#* Enter second number: 2

#* Expected Output : 
#* Sum : 12
#* Difference : 8
#* Product : 20
#* Division : 5.0

def main():
    print("Enter first number :")
    iValue1 = int(input())

    print("Enter second number :")
    iValue2 = int(input())

    Sum = lambda a, b: a + b
    print("Sum: ", Sum(iValue1, iValue2))

    Difference = lambda a, b: a - b
    print("Difference: ", Difference(iValue1, iValue2))

    Product = lambda a, b: a * b
    print("Product: ", Product(iValue1, iValue2))

    Division = lambda a, b: a / b
    print("Division: ", Division(iValue1, iValue2))

if __name__ == "__main__":
    main()