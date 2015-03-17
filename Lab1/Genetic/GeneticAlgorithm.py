__author__ = 'Joanna'
from random import randint, uniform


class GeneticAlgorithm:
    pop_size = 100
    pop_limit = 100
    num_color = 5
    num_ch = sum(1 for line in open('input.txt'))
    px = 0.5
    pm = 0.01

    def __init__(self, population):
        self.population = population
        self.new_population = []

    def initialize(self):
        for i in range(self.pop_size):
            one_individual = []
            for j in range(self.num_ch):
                one_individual.append(randint(0, self.num_color))
            self.population.append(one_individual)

    def fitness(self):
        error_list = []
        for i in self.population:
            f = open("input.txt", "r")
            out = f.readlines()
            error = 0
            for j in out:
                line = j.split(" ")
                if i[int(line[1]) - 1] == i[int(line[2]) - 1]:
                    error += 1
            error_list.append(error)
            f.close()
        return error_list

    def tournament(self):
        candidates = []
        for i in range(5):
            candidates.append(self.population[randint(0, len(self.population) - 1)])
        return candidates

    def selection(self):
        candidates = self.tournament()
        candidates_fitness = []
        for i in candidates:
            f = open("input.txt", "r")
            out = f.readlines()
            error = 0
            for j in out:
                line = j.split(" ")
                if i[int(line[1]) - 1] == i[int(line[2]) - 1]:
                    error += 1
            candidates_fitness.append(error)
            f.close()
        return candidates[candidates_fitness.index(min(candidates_fitness))]

    def crossover(self, one, two):
        new_individual = []
        if uniform(0, 1) < self.px:
            for i in range(0, self.num_ch / 2):
                new_individual.append(two[i])
            for j in range(self.num_ch / 2, self.num_ch):
                new_individual.append(one[j])
        return new_individual

    def mutation(self, individual):
        mutated = []
        for i in individual:
            if uniform(0, 1) < self.pm:
                if i == 0:
                    mutated.append(1)
                else:
                    mutated.append(0)
            else:
                mutated.append(i)
        return mutated

if __name__ == "__main__":
    ga = GeneticAlgorithm([])
    ga.initialize()
    output = open("output.txt", "w+")
    for i in range(100):
        print "Populacja nr: ", i+1
        errors = ga.fitness()
        output.write("Best, " + str(min(errors)) + ", Avg, " + str(sum(errors)/len(errors)) + ", Worst, " + str(max(errors)) + "\n")
        print "Best, ", str(min(errors)), ", Avg, " + str(sum(errors)/len(errors)), ", Worst, ", str(max(errors))
        for individual in ga.population:
            mate = ga.selection()
            child = ga.crossover(individual, mate)
            if not child:
                ga.new_population.append(ga.mutation(individual))
            else:
                ga.new_population.append(ga.mutation(child))
        ga = GeneticAlgorithm(ga.new_population)
    output.close()