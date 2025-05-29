
#?              Python Programming Assignment based on data types on conditional logic
#! Find Largest Among Three Numbers
#! Accept three numbers from user and print the largest using nested if-else statements.

#* Expected Input : 
#* Enter three numbers : 5 9 3

#* Expected Output : 
#* Largest number is 9.

def LargestNo(numData):
    if(numData[0] > numData[1]):
        if(numData[0] > numData[2]):
            print("Largest number is", numData[0], end=".")
        else:
            print("Largest number is", numData[2], end=".")
    else:
        if(numData[1] > numData[2]):
            print("Largest number is", numData[1], end=".")
        else:
            print("Largest number is", numData[2], end=".")

def main():
    print("Enter three numbers :")
    Num = list()
    for i in range(3):
        no = int(input())
        Num.append(no)
    
    LargestNo(Num)

if __name__ == "__main__":
    main()