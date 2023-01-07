import math
def area_of_circle():
    pi = 3.14
    r = int(input("Enter your radius:"))
    area = (pi *(pow(r, 2)))
    print(f"The Area of the circle is {area}")
def circumference_of_circle():
    pi = 3.14
    r = int(input("Enter radius:"))
    c = (2*pi*r)
    print( f"The circumference is {c}" )
def area_for_triangle():
    b =int(input("Enter your base:"))
    h =int(input("Enter your height:"))
    area=(1/2)*b*h
    print(f"The Area of the triangle is {area}")
def perimeter_for_triangle():
    a =int(input("Enter first side:"))
    b =int(input("Enter second side:"))
    c =int(input("Enter third side:"))
    perimeter=(a+b+c)
    print(f"The perimeter of the triangle is {perimeter}")
def area_for_rectangle():
    a=int(input("Enter the length:"))
    b=int(input("Enter the width:"))
    area=(a*b)
    print(f"The area of the rectangle is {area}")
def perimeter_for_rectangle():
     a=int(input("Enter the length:"))
     b=int(input("Enter the width:"))
     perimeter=(2(a+b))
     print(f"The perimeter of the rectangle is {perimeter}")
def area_of_square():
    a=int(input("Enter the length:"))
    area=(a*4)
    print(f"The area of the square is {area}")
def perimeter_of_square():
     a=int(input("Enter the length:"))
     perimeter=(4*a)
     print(f"The perimeter of the square is {perimeter}")
def area_for_parallelogram():
    a=int(input("Enter the base:"))
    b=int(input("Enter the vertical height:"))
    area=(b*h)
    print(f"The area of the parallelogram is {area}")
def perimeter_for_parallelogram():
     a=int(input("Enter the side:"))
     b=int(input("Enter the base:"))
     perimeter=(2*a+b)
     print(f"The area of the parallelogram is {perimeter}")
while True:
    print("""Welcome to Area and Perimeter calculator
            Enter 1 for Area of a Circle
            Enter 2 for Circumference of a Circle
            Enter 3 for area of Triangle
            Enter 4 for perimeter of Triangle
            Enter 5 for area of a rectangle
            Enter 6 for perimeter of a recctangle
            Enter 7 for area of square
            Enter 8 for perimeter of square
            Enter 9 for area of parallelogram
            Enter 10 for perimeter of parallelogram 
""")
    option = int(input("Enter your option from above:"))
    if option== 1:
        area_of_circle()
    elif option == 2:
        circumference_of_circle()
    elif option == 3:
        area_for_triangle()
    elif option == 4:
        perimeter_for_triangle()
    elif option ==5:
        area_for_rectangle()
    elif option ==6:
        perimeter_for_rectangle()
    elif option ==7:
        area_of_square()
    elif option ==8:
        perimeter_of_square()
    elif option ==9:
        area_for_parallelogram()
    elif option ==10:
        perimeter_for_parallelogram()
else :
    print("Invalid option")    
