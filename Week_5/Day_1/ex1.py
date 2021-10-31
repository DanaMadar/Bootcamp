
# # ex1
# class Cat():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduction(self):
#         print(f"The oldest cat is {self.name}, and is {self.age} years old.")


# cats = [Cat("lily", 4), Cat("Bella", 2), Cat("Büsi", 20)]


# def oldest_cat(cats):
#     cat = sorted(cats, key=lambda cat: cat.age)[-1]
#     return cat


# oldest = oldest_cat(cats)
# print(oldest.name, oldest.age)


# # ex2
# class Dog():
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

#     def bark(self):
#         print(f"{self.name} goes woof!")

#     def jump(self):
#         x = self.height*2
#         print(f"{self.name} jumps {x} cm high!")


# davids_dog = Dog("Rex", 50)
# davids_dog.bark()
# davids_dog.jump()
# sarahs_dog = Dog("Teacup", 20)
# sarahs_dog.bark()
# sarahs_dog.jump()


# def bigger(dog1, dog2):
#     if dog1.height > dog2.height:
#         return dog1
#     else:
#         return dog2


# print(f"The bigger go is: {bigger(davids_dog, sarahs_dog).name}")


# # ex3
# class Song():
#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)


# stairway = Song(["There’s a lady who's sure", "all that glitters is gold",
#                 "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()


# ex4
class Zoo():
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        self.groups = {}

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.pop(self.animals.index(animal_sold))

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        count = 1
        while len(sorted_animals) > 0:
            first_animal = sorted_animals.pop(0)
            animals = [first_animal]
            for animal in sorted_animals:
                if animal[0] == first_animal[0]:
                    animals.append(animal)
                    sorted_animals.remove(animal)
            if len(animals) == 1:
                self.groups[count] = animals[0]
            else:
                self.groups[count] = animals
            count += 1

    def get_groups(self):
        print(self.groups)


ramat_gan_safari = Zoo('ramat_gan_safari')
ramat_gan_safari.add_animal('Ape')
ramat_gan_safari.add_animal('Baboon')
ramat_gan_safari.add_animal('Bear')
ramat_gan_safari.add_animal('Cat')
ramat_gan_safari.add_animal('Cougar')
ramat_gan_safari.add_animal('Eel')
ramat_gan_safari.add_animal('Emu')

ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
