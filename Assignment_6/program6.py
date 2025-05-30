
#?              Python Programming Assignment based on Loops
#! Print Triangle Pattern using Nested Loops

#* Expected Output : 
# *
# *  *
# *  *  *
# *  *  *  *

def Display():
    for i in range(1, 5):
        for j in range(1, 5):
            if(i >= j):
                print("*", end="\t")
        
        print("\n")

def main():
    Display()

if __name__ == "__main__":
    main()


# Time Complexity : O(N^2)
# N is natural number
# Where N >= 0 and N <= Infinity