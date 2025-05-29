
#?              Python Programming Assignment based on data types on conditional logic
#! Voting Eligibility Checker
#! Accept age from the user and check whether the person is eligible to vote.(Age should be 18 or above)

#* Expected Input : 
#* Enter age : 19

#* Expected Output : 
#* Eligible to vote.

def ChkEligibility(iNo):
    bFlag = False
    if(iNo > 18):
        bFlag = True
    
    return bFlag
        
def main():
    print("Enter age :")
    iValue = int(input())

    bRet = ChkEligibility(iValue)
    if(bRet == True):
        print("Eligible to vote.")
    else:
        print("Not Eligible to vote.")

if __name__ == "__main__":
    main()