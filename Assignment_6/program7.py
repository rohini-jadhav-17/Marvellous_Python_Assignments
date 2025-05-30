
#?              Python Programming Assignment based on Loops
#! Accept 5 numbers from the user. Find and print the largest number.

#* Expected Input : 
#* Enter 5 numbers : 23 89 12 56 45

#* Expected Output : 
#* Maximum number is : 89

def Maximum(Data):
    iMax = Data[0]
    for no in Data:
        if(no > iMax):
            iMax = no
    
    return iMax

def main():
    print("Enter 5 numbers :")
    Data = list()
    for i in range(5):
        no = int(input())
        Data.append(no)
    ret = Maximum(Data)
    print("Maximum number is :", ret)

if __name__ == "__main__":
    main()


# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity