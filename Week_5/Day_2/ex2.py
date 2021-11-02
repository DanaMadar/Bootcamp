# # ex1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())


# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'


# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# # Create another cat bread. In order to do so, create a class which inherits from the Cat class.


# class Bread(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# # Create a few cat instances.
# chartreux_cat = Chartreux("mumi", 10)
# bengal_cat = Bengal("yaffa", 1)
# bread_cat = Bread("mizi", 5)
# bread_cat.sing("muaow")

# # Create a list called my_cats, which will hold all the created cat instances.
# my_cats = [chartreux_cat, bengal_cat, bread_cat]

# # Create a variable called my_pets. It’s value is an instance of the Pet class.
# my_pets = Pets(my_cats)

# # Take all the cats for a walk, use the walk method.
# my_pets.walk()


# ex2
# Create a class called Dog with the following attributes name, age, weight.
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return print(f"{self.name} is barking")

    def run_speed(self):
        speed = self.weight / self.age*10
        return print(speed)

    # def fight(self, other_dog):
    #     strength = self.run_speed() * self.weight
    #     winner = self.strength > other_dog.strength
    #     return print(winner)


dog1 = Dog("Fluffy", 15, 50)
dog2 = Dog("Stinky", 2, 10)
dog3 = Dog("fatty", 6, 100)
dog1.bark()
dog2.bark()
dog3.bark()
dog1.run_speed()
dog2.run_speed()
dog3.run_speed()
# dog1.fight(dog2)
# dog2.fight()
# dog3.fight()
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value should be another dog called other_dog, returns a string stating which dog won the fight.
# The winner should be the dog with the higher run_speed x weight.
