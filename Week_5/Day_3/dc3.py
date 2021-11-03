import turtle
circles = []
circles = circles
for i in range(2):
    unit = input("do you prefer radius or diameter? ")
    size = int(input("what size is the circle? "))

    radius = ""
    if unit == "radius":
        radius = size
    elif unit == "diameter":
        radius = size/2
    else:
        print("none of the units")

    circles.append(radius)
print(circles)

c0 = turtle.Turtle()
c1 = turtle.Turtle()
c0.circle(circles[0])
c1.circle(circles[1])


'''The goal is to create a class that represents a simple circle.
A Circle can be defined by either specifying the radius or the diameter.
The user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:


Be able to compare two circles to see which is bigger
Be able to compare two circles and see if there are equal
Be able to put them in a list and sort them'''
