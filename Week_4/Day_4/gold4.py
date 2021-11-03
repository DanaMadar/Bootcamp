import random
season = input("Which season is it?\n")


def get_random_temp(season):
    if season == "winter":
        return random.randint(-10, 10)
    elif season == "spring":
        return random.randint(10, 20)
    elif season == "summer":
        return random.randint(30, 41)
    elif season == "autumn":
        return random.randint(20, 30)


def main():
    cel = get_random_temp(season)
    print(f"The temperature right now is {cel} degrees Celsius.")
    if cel < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif cel <= 16:
        print("Quite chilly! Don’t forget your coat")
    elif cel <= 23:
        print("The temperature is getting better")
    elif cel <= 32:
        print("I'm thinking of having a swim today")
    elif cel <= 40:
        print("I'm sweatting my a** off, let's get naked!")


get_random_temp(season)
main()
