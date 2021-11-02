import random

dna = {
    1: [random.choice([0, 1]) for gene in range(10)], +
    2: [random.choice([0, 1]) for gene in range(10)], +
    3: [random.choice([0, 1]) for gene in range(10)], +
    4: [random.choice([0, 1]) for gene in range(10)], +
    5: [random.choice([0, 1]) for gene in range(10)], +
    6: [random.choice([0, 1]) for gene in range(10)], +
    7: [random.choice([0, 1]) for gene in range(10)], +
    8: [random.choice([0, 1]) for gene in range(10)], +
    9: [random.choice([0, 1]) for gene in range(10)], +
    10: [random.choice([0, 1]) for gene in range(10)]
}


class Organism():
    def __init__(self, dna, environment):
        self.dna = dna
        self.environment = environment


class Sea(Organism):
    for list in dna.values():
        dna_list = [*list]
        count = 0
        if dna_list[0] == 1:
            dna_list[-1] = 1
        elif dna_list[-1] == 1:
            dna_list[0] = 1
    dna[1] = dna_list
    print(f"these are the chromosomes an organism of the sea:\n {dna_list}\n")
    print(f"this is the dna of an organism in the sea:\n {dna}\n")

    def perfect_dna(self):
        for list in dna.values():
            count = 0
            if list != [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                count += 1
                continue
            else:
                return count


class land(Organism):
    for list in dna.values():
        dna_list = [*list]
        if dna_list[0] == 0:
            dna_list[-1] = 0
        elif dna_list[-1] == 0:
            dna_list[0] = 0
        dna[1] = dna_list

    dna.update({'1': dna_list})
    print(f"these are the genes of an organism from the land:\n {dna_list}\n")

    def dna_function(self):
        for list_value in dna.values():
            count = 0
            if list_value != [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                count += 1
                continue
            else:
                return count

    print(f"these are the genes of an organism from the land:\n {dna}\n")


creature = Organism(dna, "sea")
sea_creature = Sea(creature, "sea")
land_creature = land(creature, "land")
