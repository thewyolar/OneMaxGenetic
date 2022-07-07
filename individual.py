class Individual:
    def __init__(self, _list):
        self.chromosomes = _list
        self.fitness = 0

    def fitness(self):
        self.fitness = sum(self.chromosomes)

    def getFitness(self):
        return self.fitness

    def get(self, index):
        return self.chromosomes[index]

    def __str__(self):
        return str(self.chromosomes)

    def __len__(self):
        return len(self.chromosomes)
