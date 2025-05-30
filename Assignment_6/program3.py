
#?              Python Programming Assignment based on Loops
#! Accept a number from the user and print its multiplication table up to 10.

#* Expected Input : 
#* Enter a number : 7

#* Expected Output : 
#* 7 x 1 = 7
#* 7 x 2 = 14
#* . . .
#* 7 x 10 = 70

def Table(iNo):
    iCount = 10
    for i in range(1, iCount+1):
        print(iNo,"x",i,"=", iNo*i)

def main():
    print("Enter a number :")
    iValue = int(input())

    Table(iValue)

if __name__ == "__main__":
    main()


# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity