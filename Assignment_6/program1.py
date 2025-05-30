
#?              Python Programming Assignment based on Loops
#! Write a program using a while loop to print numbers from 1 to 50.

#* Expected Output : 
#* 1 2 3 4 . . . . 50

def Display():
    iCount = 1
    while(iCount != 51):
        print(iCount, end="\t")
        iCount += 1

def main():
    Display()

if __name__ == "__main__":
    main()

# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity