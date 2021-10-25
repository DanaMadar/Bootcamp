#ex1
print("Hello World\n"*4)


#ex2
result = (99^3) * 8
print(result)

#ex3
#false
#true
#false
#false

#ex4
computer_brand = "apple"
print("I have an " + computer_brand + " computer")

#ex5
name = "Dana"
age = "33"
shoe_size = "37"
info = "Hi my name is " + name + "I am " + age + " years old and my shoe size is " + shoe_size
print(info)

#ex6
a = 8
b = 4
if a > b:
    print("Hello World")

#ex7
num = int(input("give me a number\n"))
if num % 2 == 0:
    print("this number is even")
else:
    print("this number is odd")

#ex8
user_name = input("what's your name?\n").lower
my_name = "dana"
if user_name == my_name:
    print("you've got an amazing name")
else:
    print("your name sucks and mine is waaaaay better")

#ex9
height = float(input("What's your hieght in inch\n"))
height_cm = height * 2.54
if height_cm > 145:
    print("you're tall enough to ride")
else:
    print("Sorry, you're too small to ride")