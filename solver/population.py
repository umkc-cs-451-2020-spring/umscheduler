from .individual import Individual, Chromosome
import random

class Population(object):
    '''
    Takes a collection of Individual instances and runs them through the process of natural selection.
    '''
    def __init__(self, alleles, n_chromosomes = 1, size = 20, print_gens = False, convergence_minimum = 1, main_fitness_function = None, individual_fitness_functions = []):
        self.alleles = alleles
        self.n_chromosomes = n_chromosomes

        self.print_gen = print if print_gens else lambda x: None

        self.convergence_minimum = convergence_minimum
        self.size = size
        self.individual_fitness_functions = individual_fitness_functions
        self.normalised = False

        self.populate()
    def populate(self):
        self.population = []
        self.fitnesses = []
        self.normalised = False
        # initialise the population up to the size
        for _ in range(self.size):
            self.population.append(Individual(self.alleles, Chromosome.DEFAULT_MUT_RATE, self.n_chromosomes, self.individual_fitness_functions))
        # save the corresponding fitnesses
        self.fitnesses = [p.fitness() for p in self.population]
    
    def adjust_fitness(self):
        # square the fitnesses
        self.fitnesses = [i**2 if i > 0 else 0 for i in self.fitnesses]
        denom = sum(self.fitnesses)
        # sort the population by fitness
        self.fitnesses, self.population = zip(*sorted(zip(self.fitnesses, self.population), reverse=True, key=lambda x:x[0]))        
        self.fitnesses = [x/denom for x in self.fitnesses]
        # do a cumulative sum
        for i in range(1, len(self.fitnesses)):
            self.fitnesses[i] += self.fitnesses[i-1]
        self.normalised = True
    
    def build_next_generation(self):
        parents = zip(self.fitnesses, self.population)
        self.population = []
        self.fitnesses = []
        # build a new population up to size
        for _ in range(self.size):
            # select two parents at random
            threshold = random.random()
            father = Individual(self.alleles, Chromosome.DEFAULT_MUT_RATE, self.n_chromosomes, self.individual_fitness_functions)
            for fit, ind in parents:
                if fit >= threshold:
                    father = ind
                    break
            threshold = random.random()
            mother = Individual(self.alleles, Chromosome.DEFAULT_MUT_RATE, self.n_chromosomes, self.individual_fitness_functions)
            for fit, ind in parents:
                if fit >= threshold:
                    mother = ind
                    break
            # save the offspring
            self.population.append(father + mother)
        # save the corresponding fitnesses
        self.fitnesses = [p.fitness() for p in self.population]
    
        
    def run_until_convergence(self, threshold):
        # keep booleans of whether the condition worked
        history = [None] * self.convergence_minimum
        previous = -1.0
        best_individual = self.population[0]
        gen = 0
        # where not three in a row
        while not all(history):
            # remove the oldest
            history.pop(0)
            current, best_individual = max(*zip(self.fitnesses, self.population), key=lambda i: i[0])
            average = sum(i for i in self.fitnesses if i > 0) / len(self.fitnesses)
            
            self.print_gen('''
            Generation: {}
                Best: {}
                Average: {}
            '''.format(gen, current, average))
            # normalise values
            self.adjust_fitness()
            # advance generations
            self.build_next_generation()
            # add the newest
            history.append(abs(current - previous) / previous <= threshold)
            previous = current
            # update
            gen += 1
        
        # check violations
        best_individual.print_violations()
        return best_individual
        