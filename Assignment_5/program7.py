
#?              Python Programming Assignment based on data types on conditional logic
#! Area and Perimeter of Rectangle
#! Accept the length and width of a rectangle. Calculate and display the area and perimeter.

#* Expected Input : 
#* Enter length : 5
#* Enter width : 3

#* Expected Output : 
#* Area : 15
#* Perimeter : 16

def AreaPerimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    
    return area, perimeter

def main():
    print("Enter length :")
    length = int(input())

    print("Enter width :")
    width = int(input())
    
    area, perimeter = AreaPerimeter(length, width)
    print("Area :", area)
    print("Perimeter :", perimeter)

if __name__ == "__main__":
    main()