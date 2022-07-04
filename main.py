from random import randint
import matplotlib.pyplot as plt

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


if __name__ == '__main__':
    population = createPopulation(POPULATION_SIZE)
    counter = 0

    fitness = [population[i].fitness for i in range(len(population))]
    print(sum(fitness))
