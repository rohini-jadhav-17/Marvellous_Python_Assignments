
#?              Python Programming Assignment based on Loops
#! Accept a number from the user and print its factorial using for loop.

#* Expected Input : 
#* Enter a number : 5

#* Expected Output : 
#* Factorial of 5 is : 120

def Factorial(iNo):
    iFact = 1
    for i in range(iNo, 0, -1):
        iFact = iFact * i
    
    return iFact

def main():
    print("Enter a number :")
    iValue = int(input())

    ret = Factorial(iValue)
    print("Factorial of ", iValue, "is :", ret)

if __name__ == "__main__":
    main()


# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity