# ex3
from ex2 import Dog
import random


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.trained = True
        self.bark()

    def play(self, *args):
        print(f"{args} all play together")

    def do_a_trick(self):
        if self.trained:
            print(f"{self.name}" + random.choice([" does a barrel roll", " stands on his back legs",
                                                  " shakes your hand", " plays dead"]))


pet_dog1 = PetDog("maria", 2, 20, True)
pet_dog2 = PetDog("pete", 4, 21, True)
pet_dog3 = PetDog("may", 90, 200, True)

pet_dog1.bark()
pet_dog1.play("maria", "pete", "may")
pet_dog1.do_a_trick()
