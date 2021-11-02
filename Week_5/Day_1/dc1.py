class Farm:
    def __init__(self, name):
        self.animals = {}
        self.name = name

    def add_animal(self, name, amount=1):
        if name in self.animals:
            self.animals[name] += amount
        else:
            self.animals[name] = amount

    def get_info(self):
        str = ''
        for animal in self.animals:
            str += f'{animal}: {self.animals[animal]}\n'
        str += f'\n\tE-I-E-I-0!'
        return str

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        str = "McDonald's farm has: \n"
        animal_types = self.get_animal_types()

        for animal in animal_types:
            if animal_types.index(animal) == 0:
                str += f' {animal}'
            elif animal_types.index(animal) == len(animal_types)-1:
                str += f' and {animal}'
            else:
                str += f' ,{animal}'

        return str


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
print(macdonald.animals)
