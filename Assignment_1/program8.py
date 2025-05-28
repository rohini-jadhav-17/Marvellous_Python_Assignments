
#! Write a program which accept number from user and print that number of "*" on screen.

#Input : 5     Output :   *   *   *   *   *

def Display(iNo):
    for i in range(iNo):
        print("*\t", end=" ")

def main():
    print("Enter number :")
    iValue = int(input())

    Display(iValue)

# Starter function
if __name__ == "__main__":
    main()