
#?              Python Programming Assignment based on data types on conditional logic
#! Celsius to Fahrenheit converter
#! Accept temperature in Celsius and convert it to Fahrenheit using formula:
#! F = (C * 9/5) + 32

#* Expected Input : 
#* Enter temperature in celsius : 25

#* Expected Output : 
#* Temperature in Fahrenheit : 77.0 °F

def CtoFConverter(iNo):
    fTemp = ((iNo * 9) / 5) + 32
    
    return fTemp        

def main():
    print("Enter temperature in celsius :")
    iValue = int(input())
    
    ret = CtoFConverter(iValue)
    print("Temperature in Fahrenheit :", ret, "°F.")

if __name__ == "__main__":
    main()