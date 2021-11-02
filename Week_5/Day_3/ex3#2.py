import datetime
import time

# # ex1
# now = datetime.datetime.now()
# print(now.strftime(f"The current date is: %d-%m-%Y"))

# # ex2


# def timer():
#     endTime = datetime.datetime(2022, 1, 1, 0, 0, 0)
#     return endTime


# def countdown():
#     return timer() - now


# print(countdown())

# # ex3
# while True:
#     try:
#         bday = input("Please enter your exact Date of Birth:\n")
#         birthday = datetime.datetime.strptime(bday, '%d %m %Y')
#         break
#     except:
#         print("Please put in the Format 'Day Month Year' without any initial space")

# tday = datetime.datetime.today()
# time_in_sec = (tday - birthday).total_seconds()
# print("You have been alive for:", time_in_sec, "seconds")

# # ex4


# def timer():
#     Chanukka = datetime.datetime(2021, 11, 29, 0, 0, 0)
#     return Chanukka


# def countdown():
#     return timer() - now


# print(f"Chanukka is in: {countdown()}")

# ex5
earth_year = 31557600
planets = {
    "earth": 1,
    "mercury": earth_year*0.2408467,
    "venus": earth_year*0.61519726,
    "mars": earth_year*1.8808158,
    "jupiter": earth_year*11.862615,
    "saturn": earth_year*29.447498,
    "uranus": earth_year*84.016846,
    "neptun": earth_year*164.79132
}

years = input("how old are you? ")
input_planet = input(
    "on which planet do you wanna know your age?\n(mercury, venus, earth, mars, jupiter, saturn, uranus or neptun)").lower()

years = float(years)/earth_year
print(f'On {input_planet} you are {planets[input_planet]*years} yeras old!!!')
