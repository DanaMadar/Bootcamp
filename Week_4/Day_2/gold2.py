#ex1
# list_1 = ["j","d","q"]
# list_2 = ["x","c","v"]
# list_1.extend(list_2)
# print(list_1)

#ex2
# greatest_number = 0
# i = 0
# while i < 3:
#     user_input = int(input("give me a number: "))
#     if user_input > greatest_number:
#         greatest_number =  user_input
#     i += 1

# print(f"This is the greatest number: {greatest_number}")

#ex3
# letter_list = ["w", "e", "s", "a"]
# vowles = ["a", "e", "i", "o", "u"]

# for letter in letter_list:
#     if letter in vowles:
#         print("this is a vowle")
#     else:
#         print("this is not a vowle")

#ex4
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("type in a name: ")


for same in names:
    if same == user_name:
        print(f"the user name is {same}, and the index is {names.index(same)}.")
