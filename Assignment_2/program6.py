
#! Write a program which accept one number and display below pattern.

#Input  :   5
#Output :   *   *   *   *   *
#           *   *   *   *   
#           *   *   *   
#           *   *   
#           *   

def Display(iNo):
    for i in range(1, iNo+1):
        for j in range(iNo, 0, -1):
            if(i <= j):
                print("*", end = "\t")
        print("\n")

def main():
    print("Enter number :")
    iValue = int(input())

    Display(iValue)

# Starter function
if __name__ == "__main__":
    main()