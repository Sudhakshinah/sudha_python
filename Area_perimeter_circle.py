class Circle:

    def __init__(self, r):
        self.pi = 3.14
        self.radius = r

    # Method to find the area of circle

    def area_circle(self):
        return round(self.pi * self.radius * self.radius,2)

    # Method to find the Perimeter of the circle

    def perimeter_circle(self):
        return round(2 * self.pi * self.radius,2)


input_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Empty result to append the area and perimeter  of each member of the list

area = []
perimeter =[]

# Loop through the list to find the area by area method defined above

for i in range(0, 8):
    ac = Circle(input_list[i]).area_circle()
    area.append(ac)
print(f" The area  is {area}")


# Loop through the input list to find the perimeter by perimeter method

for i in range(0, 8):
    pc = Circle(input_list[i]).perimeter_circle()
    perimeter.append(pc)
print(f" The perimeter is {perimeter}")












