
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
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        '''This method adds the new_animal 
        to the animals list as long as it isn't already in the list.'''
        if not new_animal in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        '''prints all the animals of the zoo.'''
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        '''removes the animal from the list if it exists in the list.'''
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        '''Create a method called sort_animals that sorts the animals
         alphabetically and groups them together based on their first letter.'''
        animals_lists = []
        for animal in sorted(self.animals):
            if not animals_lists:
                animals_lists.append([animal])

            else:
                if animal[0] == animals_lists[-1][0][0]:
                    animals_lists[-1].append(animal)
                else:
                    animals_lists.append([animal])

            print(animals_lists)


ramat_gan_safari = Zoo('Ramat Gan Safari')
for animal in ['Cat', 'Cougar', "Baboon", 'Eel', 'Emu', "Baboon", "Baboon", "Baboon", "Bear", "Ape", ]:
    ramat_gan_safari.add_animal(animal)

ramat_gan_safari.sort_animals()
