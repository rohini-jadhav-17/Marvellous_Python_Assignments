
#! Write a program which accept name from user and display length of its name

#Input : Marvellous          Output :  10

def DisplayLength(sName):
    count = 0
    for i in sName:
        count += 1
    print(count)

def main():
    print("Enter name :")
    sValue = input()

    DisplayLength(sValue)

# Starter function
if __name__ == "__main__":
    main()