# #ex1
# my_fav_numbers = {5,4,3}
# my_fav_numbers.add(9)
# my_fav_numbers.add(1)
# my_fav_numbers.pop()
# print(my_fav_numbers)


# friend_fav_numbers = {0, 4, 3, 8}

# our_fav_numbers = my_fav_numbers | (friend_fav_numbers) #add 2 tuples together
# # my_fav_numbers.update(friend_fav_numbers)
# print(our_fav_numbers)

#ex2
#not changable

#ex3

# number = range(1, 21)
# for n in number:
#   print(n)

#ex4

# i = 1.0
# while i < 6:
#   print(i)
#   i += 0.5

#ex5
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.pop()
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# count = basket.count("Apples")
# basket.clear()


# print(basket)

#ex6
# my_name = "dana"
# user_name = input("type in a name: ")

# while my_name != user_name:
#     user_name = input("find my name ")

# print("you made it!")


#ex7
# numbers = range(1, 21)
# for num in numbers:
#     if num % 2 == 0:
#         print("these are the even numbers : ", num)

#ex8
# numbers = range(1500, 2501)
# for num in numbers:
#     if num % 5 == 0 or num % 7 == 0:
#         print(num)

#ex9
# fruits = input("enter your favorit fruits with a space inbetween \n")
# any_fruit = input("what fruit are you thinking of right now\n")

# if fruits.find(any_fruit) != -1:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")

#ex10
# toppings = ""

# while True:
#     toppings += input("add up to 10 toppings with an space inbetween. once you're done write 'quit'\n")
#     if "quit" in toppings:
#         break

# new_toppings= toppings.split(" ")

# price =(len(new_toppings)-1) * 2.5
# print("the total price of your pizza is : ", price)

#ex11!
# ages = input("hey there! What are your ages(split by ',') ").split(",")

# price = 0
# teen_counter = 0

# for age in ages:
#     age = int(age)

#     if 16 < age <21:
#         teen_counter += 1

#     if age < 3:
#         price += 0
#     elif age < 12:
#         price += 10
#     else:
#         price += 15

# print("the total price is ", price)
# print(teen_counter)

#ex12!

# teens = ("Benny", "Sharon", "Sarah", "Lea")
# final = []

# for teen in teens:
#     age = int(input("what is your age: "))
#     if age > 16:
#         final.append(teen)

# print(final)

    
#13/14

sandwich_orders = ["tuna sandwich", "cheese sandwich", "vegan sandwich","pastrami sandwich", "pastrami sandwich", "pastrami sandwich"]
finished_sandwiches = []
print("the deli has run out of pastrami")

while "pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("pastrami sandwich")

for san in sandwich_orders:
    finished_sandwiches.append(san)

print("I made your tuna sandwich and " + "," .join(sandwich_orders))
