from random import random, randint
import matplotlib.pyplot as plt
from individual import Individual

# Constants
STRING_MAX_LENGTH = 100
POPULATION_SIZE = 200
CROSSING_PROBABILITY = 0.9
MUTATION_PROBABILITY = 0.1
MAX_GENERATIONS = 50


def createIndividuals():
    return Individual([randint(0, 1) for _ in range(STRING_MAX_LENGTH)])


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

        offspring.append(max([population[i1], population[i2], population[i3]], key=lambda ind: ind.fitness))

    return offspring


def cxOnePoint(child1, child2):
    s = randint(2, len(child1) - 3)
    child1.chromosomes[s:], child2.chromosomes[s:] = child2.chromosomes[s:], child1.chromosomes[s:]


def mutFlipBit(mutant, indpb=0.01):
    for i in range(len(mutant)):
        if random() < indpb:
            mutant[i] = 0 if mutant[i] == 1 else 1


if __name__ == '__main__':
    population = createPopulation(POPULATION_SIZE)
    counter = 0

    fitness = [population[i].getFitness() for i in range(len(population))]
    maxFitnessValues = []
    meanFitnessValues = []

    fitness = [individual.getFitness() for individual in population]

    while max(fitness) < STRING_MAX_LENGTH and counter < MAX_GENERATIONS:
        counter += 1
        offspring = selTournament(population, len(population))
        offspring = list(map(clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random() < CROSSING_PROBABILITY:
                cxOnePoint(child1, child2)

        for mutant in offspring:
            if random() < MUTATION_PROBABILITY:
                mutFlipBit(mutant, indpb=1.0 / STRING_MAX_LENGTH)

        freshFitnessValues = list(map(individual.getFitness(), offspring))

        for individual, fitnessValue in zip(offspring, freshFitnessValues):
            individual.fitness.values = fitnessValue

        population = offspring

        fitnessValues = [ind.fitness.values[0] for ind in population]

        maxFitness = max(fitnessValues)
        meanFitness = sum(fitnessValues) / len(population)
        maxFitnessValues.append(maxFitness)
        meanFitnessValues.append(meanFitness)
        print(f"Поколение {counter}: Макс приспособ. = {maxFitness}, Средняя приспособ.= {meanFitness}")

        best_index = fitnessValues.index(max(fitnessValues))
        print("Лучший индивидуум = ", population[best_index], "\n")

    plt.plot(maxFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Поколение')
    plt.ylabel('Макс/средняя приспособленность')
    plt.title('Зависимость максимальной и средней приспособленности от поколения')
    plt.show()
