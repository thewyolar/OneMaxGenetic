class Individual(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.fitness = sum(self)

    def getFitness(self):
        return self.fitness
