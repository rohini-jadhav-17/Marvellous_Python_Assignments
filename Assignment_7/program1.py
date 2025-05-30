
#?              Python Programming Assignment based on Lambda functions
#! Write two lambda functions:
#! ● One to calculate square of number
#! ● Another to calculate cube of number

#* Expected Input :
#* Enter a number : 3

#* Expected Output :
#* Square : 9
#* Cube : 27

Square = lambda x: x*x

Cube = lambda x: x*x*x

def main():
    print("Enter a number :")
    iValue = int(input())

    result = Square(iValue)
    print("Square :", result)

    result = Cube(iValue)
    print("Cube :", result)

if __name__ == "__main__":
    main()