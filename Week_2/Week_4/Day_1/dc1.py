# import random

# user_str = input("type in a string of 10 characters\n")

# if len(user_str) < 10:
#     print("string not long enough")
# elif len(user_str) < 10:
#     print("string too long")

# print(user_str[0] + user_str[-1])

# list = list(user_str)
# new_str = ""
# print(list)
# for i in list:
#     new_str += i
#     print(new_str)


# random.shuffle(list)
# print(list)

input1 = 0
input2 = 0
input3 = ""

if input1 or input2 == False and input3 != 'add'or 'multiply' or 'divide':
    input1 = float(input("give me a number\n"))
    input2 = float(input("give me another number\n"))
    input3 = input("give me an operator as 'add', 'multiply', 'divide'\n")

my_sum = 0

if input3 == "add":
    my_sum = input1 + input2
elif input3 == "multiply":
    my_sum = input1 * input2
elif input3 == "divide":
    my_sum = input1 / input2


if input1 == input2:
    print("number1 with the power of number2")
else:
    print(my_sum)

