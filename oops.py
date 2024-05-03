#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.


# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         print(f"the area of the circle is {3.14 * self.radius**2}")
    
#     def perimeter(self):
#         print(f"the perimeter of the square is { 2 * 3.14 * self.radius }")

# radi = int(input("enter the radius"))
# obj1 = Circle(radi)
# obj1.area()
# obj1.perimeter()



#Write a Python program to create a person class. Include attributes  like name, country and date of birth. Implement a method to  determine the person’s age. 

# class Person:
#     def __init__(self,name,country,year):
#         self.name = name
#         self.country=country
#         self.year=year
    
#     def calculate_age(self,presentyear):
#         return (presentyear - self.year)
    
# obj1 = Person("daran","india",1996)
# print(obj1.calculate_age(2024))







#Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

# class Calculator:
#     def add(self, a, b):
#         self.a = a
#         self.b = b
#         return a + b

#     def subtract(self):
#         return self.a - self.b

#     def multiply(self):
#         return self.a * self.b

#     def divide(self):
#         if self.b == 0:
#             return "Error: Division by zero!"
#         else:
#             return self.a / self.b

# # Example usage:
# calculator = Calculator()

# print("Addition:", calculator.add(5, 3))
# print("Subtraction:", calculator.subtract())
# print("Multiplication:", calculator.multiply())
# print("Division:", calculator.divide())












#Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square. 

class Shape:
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  #pi(r)2
        return 3.14 * self.radius ** 2

    def perimeter(self): #2*pi*r
        return 2 * 3.14 * self.radius
    



class Triangle(Shape):
    def __init__(self, side1, side2, side3,base,height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.base = base
        self.height = height

    def area(self): #1/2bh
        return 0.5 * self.base * self.height

    def perimeter(self): #a+b+c
        return self.side1 + self.side2 + self.side3
    



class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self): #(a)2
        return self.side ** 2

    def perimeter(self): #4a
        return 4 * self.side
    



circle = Circle(5)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

triangle = Triangle(3, 4, 5,7,8)
print("Triangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())

square = Square(4)
print("Square Area:", square.area())
print("Square Perimeter:", square.perimeter())

