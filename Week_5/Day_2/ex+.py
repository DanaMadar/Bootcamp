# ex1
class Family():
    def __init__(self, member):
        self.member = []
        self.last_name = "Hagari"

    def born(self, **kwargs):
        print(kwargs)

        self.member.append(kwargs)

    def is_18(self, name):
        for value in self.member:
            if value["name"] == name:
                if value["age"] >= 18:
                    return True

        return False

    def membersPrint(self):
        for individual in Family.fam:
            print(individual)


fam = Family(member=[
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
])
fam.born(name="Ben", age=0, gender="Male", is_child=True)


# ex2


class TheIncredibles(Family):
    def __init__(self, member, power, incredible_name, age):
        super().__init__(member)
        self.power = power
        self.incredible_name = incredible_name
        self.age = age

    def use_power(self):
        if self.age >= 18:
            print(self.power)

    def incredible_presentation(self):
        print(
            f"my hero name is {self.incredible_name} and my super power is: {self.power}")

    def add(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    add("Jack jack")


Peter = TheIncredibles("Father", "super-strength", "Mr. Incredible", 42)
Helen = TheIncredibles("Mother", "body elasticity", "Elastigirl", 40)
Jessica = TheIncredibles(
    "Daughter", "invisibility and force fields", "Violet", 20)
Jacob = TheIncredibles("Son", "super speed", "Dash", 16)

Helen.use_power()
Peter.incredible_presentation()
Jessica.incredible_presentation()
Jacob.incredible_presentation()
