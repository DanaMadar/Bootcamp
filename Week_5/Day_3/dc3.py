import turtle
circles = []
circles = circles.sort()
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
