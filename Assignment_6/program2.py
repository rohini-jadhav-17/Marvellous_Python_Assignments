
#?              Python Programming Assignment based on Loops
#! Print Sum of Even Numbers between 1 and 100. Use a loop to find and print the sum of all even numbers from 1 to 100.

#* Expected Output : 
#* Sum of even numbers between 1 to 100 is : 2550

def SumEven():
    iCount = 100
    iSum = 0
    for i in range(iCount+1):
        if(i % 2 == 0):
            iSum = iSum + i
    
    return iSum

def main():
    ret = SumEven()
    print("Sum of even numbers between 1 to 100 is :", ret)

if __name__ == "__main__":
    main()


# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity