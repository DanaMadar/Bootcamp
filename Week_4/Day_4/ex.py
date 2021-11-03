# import random

# #ex1
# def display_message():
#     print("we learned functions today")

# display_message()


# #ex2
# def favorite_book(title):
#     print(f"One of my favorite books is {title}")

# favorite_book("Alice in Wonderland")
# favorite_book("harry potter".title())


# #ex3
# def describe_city(city, country):
#     print(f"{city} is in {country}")

# describe_city("Zurich", "Switzerland")

# #ex4
# def compare(my_num):
#     random_num = random.randint(0, 100)
#     if random_num == my_num:
#         print("you made it")
#     else:
#         print("you lost")

# compare("random.randint(0, 100)")

# ex5

# def make_shirt(size, text):

#     print(f'your shirt size is {size} and the print says {text}')


# size = "S"
# text = "Small,but feeling tall"
# make_shirt(size="L", text="I love python")
# make_shirt(size="M", text="I love python")
# make_shirt(size, text)

# ____________note to myself__________

# def make_shirt(size, text):
#     for shirt, content in zip(size, text):
#         print(f'your shirt size is {shirt} and the print says {content}')


# size = ["S", "M", "L"]
# text = ["Small,but feeling tall", "Medium, but not mediocar", "Large, you already know what that means ;)"]
# make_shirt(size, text)


# ex6

# def show_magicians():
#     for magician in magicians:
#         print(magician)

# def make_great():
#     for i in range(0, len(magicians)):
#         magicians[i] += "The Great"
#     return magicians

# magicians = ["Magic Mike", "Urli Geller", "Magicaaaaal"]
# make_great()
# show_magicians()


# ex7

# from datetime import datetime, date

# gender = print(input("which gender are you: 'f' or 'm'\n"))
# date_of_birth = datetime.strptime(
#     input("what's your gate of birth?\n"), "%d %m %Y")


# def get_age(date_of_birth):
#     today = date.today()
#     return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))


# def can_retire(gender, age):
#     if gender == "f" or age > 62:
#         print("you are retired")
#         return True
#     elif gender == "m" or age > 67:
#         print("you are retired")
#         return True
#     else:
#         print("Only a few more years")


# age = get_age(date_of_birth)
# can_retire(gender, age)

# ex8

def x_func(x):
    nums = [x, x+x, x+x+x, x+x+x+x]
    nums = list(map(int, nums))
    return (sum(nums))


print(x_func("9"))
