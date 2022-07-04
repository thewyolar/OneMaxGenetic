class Individual:
    def __init__(self, list):
        self.fitness = sum(list)
        self.chromosomes = list

    def __str__(self):
        return str(self.chromosomes)