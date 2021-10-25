#ex1
h1 = "Hello World "
h2 = "I love python "
print((4 * h1) ,(4 * h2))

#ex2
month = int(input("type in a month\n"))
if month <= 3:
    print("spring")
elif month >= 6:
    print("summer")
elif month >= 9:
    print("autumn")
elif month <= 12 or month <= 1 and month <=2:
    print("winter")