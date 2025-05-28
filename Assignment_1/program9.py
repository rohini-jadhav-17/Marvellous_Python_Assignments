
#! Write a program which display first 10 even numbers on screen.

# Output :   2  4   6   8   10  12  14  16  18  20

def DisplayEven(iNo):
    for i in range(iNo, 22, 2):
        print(i,end = "\t")

def main():
    print("Enter number :")
    iValue = int(input())

    DisplayEven(iValue)

# Starter function
if __name__ == "__main__":
    main()