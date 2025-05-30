
#?              Python Programming Assignment based on Loops
#! Accept a number from the user and check whether it is prime or not.

#* Expected Input : 
#* Enter a number : 11

#* Expected Output : 
#* 11 is a prime number

def Prime(iNo):
    stop = int(iNo / 2)
    bFlag = True
    for i in range(2, stop+1):
        if(iNo % i == 0):
            print(stop, iNo, i)
            bFlag = False
            
    return bFlag

def main():
    print("Enter a number :")
    iValue = int(input())

    bRet = Prime(iValue)
    if(bRet == True):
        print(iValue, "is a Prime number.")
    else:
        print(iValue, "is not a Prime number.")

if __name__ == "__main__":
    main()


# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity