name = input("what's your name?")
age = input("what's your age")
if age.isnumeric():
    age = int(age)

else:
    print("this is not a number")
    exit()

print(name + " is " + str(age) + " " + "years old")
intro_sentence = f"hello my name is {name} and I am {age} old"
intro_sentence2 = "hello my name is {}, I am {} yeas old".format(name, age)

print(intro_sentence)
print(intro_sentence2)

if age > 30 or name == "ben":
    print("you are amazing")
else:
    print("pfffff.. so young")
print("done")


cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

num = int(input("type in any number between 1 an 100"))
if num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")