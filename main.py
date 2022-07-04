from random import randint
from individual import Individual

# Constants
STRING_LENGTH = 100
POPULATION_SIZE = 200
CROSSING_PROBABILITY = 0.9
MUTATION_PROBABILITY = 0.1
MAX_GENERATION = 50


def createIndividuals():
    return Individual([randint(0, 1) for _ in range(STRING_LENGTH)])


def createPopulation(n=0):
    return list([createIndividuals() for _ in range(n)])


def clone(chromosomes):
    ind = Individual(chromosomes)
    return ind

def selTournament(population, size):
    offspring = []
    for i in range(size):
        i1 = i2 = i3 = 0
        while i1 == i2 or i1 == i3 or i2 == i3:
            i1, i2, i3 = randint(0, size - 1), randint(0, size - 1), randint(0, size - 1)

        offspring.append(max([population[i1], population[i2], population[i3]], key=lambda i: i.))

    return offspring


if __name__ == '__main__':
    population = createPopulation(POPULATION_SIZE)
    counter = 0

    fitness = [population[i].fitness for i in range(len(population))]
    maxFitness = []
    meanFitness = []


