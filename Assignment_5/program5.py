
#?              Python Programming Assignment based on data types on conditional logic
#! Even or Odd Number Check
#! Write a program to check whether the entered number is even or odd.

#* Expected Input : 
#* Enter a number : 17

#* Expected Output : 
#* 17 is an odd number.

def CheckEven(iNo):
    bFlag = False
    if(iNo % 2 == 0):
        bFlag = True
    
    return bFlag        

def main():
    print("Enter a number :")
    iValue = int(input())
    
    bRet = CheckEven(iValue)
    if(bRet == True):
        print(iValue, "is an even number.")
    else:
        print(iValue, "is an odd number.")

if __name__ == "__main__":
    main()