
#?              Python Programming Assignment based on data types on conditional logic
#! Vowel or Consonant check
#! Accept a single character from the user and check if it is vowel(a, e, i, o, u). If not print its a consonant.

#* Expected Input : 
#* Enter a character : e

#* Expected Output : 
#* 'e' is a vowel

def ChkVowel(cValue):
    bFlag = False
    if(cValue == 'a' or cValue == 'e' or cValue == 'i' or cValue == 'o' or cValue == 'u' or
        cValue == 'A' or cValue == 'E' or cValue == 'I' or cValue == 'O' or cValue == 'U'):
        bFlag = True
    
    return bFlag
        
def main():
    print("Enter a character :")
    cValue = str(input())

    bRet = ChkVowel(cValue)
    if(bRet == True):
        print("'", cValue, "' is a vowel.")
    else:
        print("'", cValue, "' is a consonant.")

if __name__ == "__main__":
    main()