
#?              Python Programming Assignment based on Lambda functions
#! Write a function that accepts a string and checks whether it is a palindrome.

#* Expected Input :
#* Enter a string : radar

#* Expected Output :
#* radar is a palindrome.

def Palindrome(no):
    bFlag = False
    for i, char in enumerate(no):
        if(no[i] != no[len(no)-i-1]):
            bFlag = False
            break
        else:
            bFlag = True
    
    return bFlag

def main():
    print("Enter a string :")
    
    no = str(input())
    
    ret = Palindrome(no)
    
    if(ret == True):
        print(no, "is a palindrome.")
    else:
        print(no, "is not a palindrome.")

if __name__ == "__main__":
    main()


# Time Complexity : O(N)
# N is natural number
# Where N >= 0 and N <= Infinity