# It's a simple program for calculating the AREA OF A CIRCLE
# import math since it contains the value of pi
import math

# Title
print("AREA OF A CIRCLE")
# create the class that will contains the method of calculating
class area_of_circle():
    # instantiate the class
    def __init__(self, radius):
        self.radius = radius

    # the formula for calculating the area of the circle
    def calculate(self):
        return math.pi*(self.radius**2)

# user is requested to enter the radius of the circle
ask_radius = int(input("Enter Radius of the Circle in numbers(don't use alphabets): "))

# add the input radius to the class
area = area_of_circle(ask_radius)

# call the calculate function to calculate the area and assign it to a variable
answer = area.calculate()

# print the answer
print("The radius of the Circle is: " + str(answer))
