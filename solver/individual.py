import random
from copy import copy
from math import sqrt
from enum import Enum
from typing import Union, List, Callable, Iterable

class FitnessFunctorType(Enum):
    MUL = float.__mul__
    ADD = float.__add__

class FitnessFunctor(Callable):
    '''
    Object passed to individuals or groups to enhance their fitness values.
    '''
    NO_CONSTRAINTS: list = []
    def __init__(self, operation: FitnessFunctorType, f: Callable, requirements = []):
        self.__call__ = f
        self.call = f
        self.apply = f
        self.operation = operation
        self.groups = requirements

class Chromosome(object):
    '''
    Object used to hold a collection of genes, and propagate them in crossover.
    '''
    DEFAULT_MUT_RATE = 0.005
    def __init__(self, alleles, mut_rate):
        self.alleles = alleles
        self.genes = [allele.generate() for allele in alleles]
        self.mut_rate = mut_rate
        self.__add__ = self.cross
    
    def cross(self, other) -> type:
        child = copy(self)
        self.genes = []
        # pair up the genes
        for parent_genes in zip(self.genes, other.genes):
            # choose one side
            child_gene = random.choice(parent_genes)
            # mutate, sometimes
            if child_gene.mutable() and self.will_mutate():
                child_gene.mutate()
            child.genes.append(child_gene)

        return child

    def will_mutate(self) -> bool:
        return random.random() < self.mut_rate

    def __iter__(self):
        return self.genes.__iter__()
    
    def __getitem__(self, i: int):
        return self.genes[i]
    
    def get_gene(self, gene):
        for i in self:
            if i.name == gene:
                return i
        return [allele.generate() for allele in self.alleles if allele.name == gene][0]
    
    def binary(self) -> bin:
        pass


class Individual(object):
    '''
    Object holding a collection of Chromosomes in order to evaluate fitness and mate.
    '''
    def __init__(self, alleles, mut_rate, n_chromosomes = 1, fitness_functions = []):
        self.alleles = alleles
        self.chromosomes = []
        for _ in range(n_chromosomes):
            self.chromosomes.append(Chromosome(self.alleles, mut_rate))
        self.mut_rate = mut_rate
        self.fitness_functions = fitness_functions
    
    def add_fitness_function(self, fitness_function):
        self.fitness_functions.append(fitness_function)
    
    def add_fitness_functions(self, fitness_functions):
        self.fitness_functions.extend(*fitness_functions)

    def mate(self, other) -> type:
        child = copy(self)
        child.chromosomes = []
        # if incompatible
        if self.alleles != other.alleles:
            raise TypeError("Individuals have different alleles")
        
        # pair the chromosomes together
        for parent_chromosomes in zip(self.chromosomes, other.chromosomes):
            # do the crossover for each chromosome
            child_chromosome = Chromosome.cross(*parent_chromosomes)
            child.chromosomes.append(child_chromosome)

        return child
    
    def __add__(self, other):
        return self.mate(other)

    def print_violations(self):
        enrollments = {
            'CS101A':40,
            'CS101B':25,
            'CS201A':30,
            'CS201B':30,
            'CS191A':60, 
            'CS191B':20, 
            'CS291B':40, 
            'CS291A':20, 
            'CS303':50, 
            'CS341':40, 
            'CS449':55, 
            'CS461':40
        }

        lectures = {
            'Hare': {'CS101A', 'CS101B', 'CS201A', 'CS201B', 'CS291A', 'CS291B', 'CS303', 'CS449', 'CS461'},
            'Bingham': {'CS101A', 'CS101B', 'CS191A', 'CS191B', 'CS201A', 'CS201B', 'CS291A', 'CS291B', 'CS449'},
            'Kuhail': {'CS303', 'CS341'},
            'Mitchell': {'CS191A', 'CS191B', 'CS291A', 'CS291B', 'CS303', 'CS341'},
            'Rao': {'CS291A', 'CS291B', 'CS303', 'CS341', 'CS461'}
        }

        capacities = {
            'HAAG301':70,
            'HAAG206':30,
            'ROYALL204':70,
            'KATZ209':50,
            'FLARSHEIM310':80,
            'FLARSHEIM260':25,
            'BLOCH0009':30
        }

        unique_timeslots = True
        qualified_teach = True
        room_large_enough = True
        sane_schedule = True

        def negator(x):
            return 'not ' if x else ''

        uniques = {}
        for chromosome in self.chromosomes:
            course = self.alleles[0][chromosome.get_gene('course').value]
            teach = self.alleles[1][chromosome.get_gene('instructor').value]
            room = self.alleles[2][chromosome.get_gene('room').value]
            time = self.alleles[3][chromosome.get_gene('time').value]
            # if unique time
            if uniques.get((room, time)) is None:
                uniques[(room, time)] = 1
            else:
                # if not
                if uniques[(room, time)] == 1:
                    unique_timeslots = False
                uniques[(room, time)] += 1
            # if course could not be found in the professor's course list
            if not course in lectures[teach]:
                qualified_teach = False
            
            # if over capacity
            if enrollments[course] > capacities[room]:
                room_large_enough = False
            
            # if the teacher section is unique
            if uniques.get((teach)) is None:
                uniques[(teach)] = 1
            else:
                # teaches more than one section
                uniques[(teach)] += 1
                if uniques.get((teach)) > 4:
                    # more than 4
                    sane_schedule = False
        
        num_violations = sum(int(i) for i in (unique_timeslots, qualified_teach, room_large_enough, sane_schedule))
        violations = "\n{} violation(s) found.\nThere are {}classes in the same room at the same time.\nThe instructors are {}qualified to teach.\nThe rooms can {}fit the expected enrollments.\nThere are {}instructors with more than four courses.".format(num_violations, negator(not unique_timeslots), negator(qualified_teach), negator(room_large_enough), negator(not sane_schedule))
        print(violations)
            

                


    def fitness(self) -> Union[int, float]:

        enrollments = {
        }

        lectures = {
        }

        capacities = {
        }
        rooms = capacities.keys()
        times = [10, 11, 12, 13, 14, 15, 16]

        fitness_value = 0.0
        multiplier = 100

        uniques = {}
        for chromosome in self.chromosomes:
            course = self.alleles[0][chromosome.get_gene('course').value]
            teach = self.alleles[1][chromosome.get_gene('instructor').value]
            room = self.alleles[2][chromosome.get_gene('room').value]
            time = self.alleles[3][chromosome.get_gene('time').value]
            # if instructor qualified
            if course in lectures[teach]:
                fitness_value += 5
            # counting course with time
            if uniques.get((course, time)) is None:
                uniques[(course, time)] = 1
            else:
                uniques[(course, time)] += 1
            # counting room with time
            if uniques.get((room, time)) is None:
                fitness_value += 5
                uniques[(room, time)] = 1
            else:
                if uniques[(room, time)] == 1:
                    fitness_value -= 5
                uniques[(room, time)] += 1
            # counting course with room and time
            if uniques.get((course, room, time)) is None:
                uniques[(course, room, time)] = 1
            else:
                uniques[(course, room, time)] += 1
            # if within capacity
            if enrollments[course] <= capacities[room]:
                fitness_value += 5
                if enrollments[course] * 2 > capacities[room]:
                    fitness_value += 2
            # counting teacher with time
            if uniques.get((teach, time)) is None:
                fitness_value += 5
                uniques[(teach, time)] = 1
            else:
                if uniques.get((teach, time)) == 1:
                    fitness_value -= 5
                uniques[(teach, time)] += 1
            # counting # of courses for teacher
            if uniques.get((teach)) is None:
                uniques[(teach)] = 1
            else:
                uniques[(teach)] += 1
                if uniques.get((teach)) > 4:
                    fitness_value -= 5
            gradTotal = uniques.get(('XGrad'), 0) + uniques.get((''), 0)
            notGradTotal = uniques.get(('X'), 0) + uniques.get((''), 0)
            if gradTotal > notGradTotal:
                multiplier -= 5
            if gradTotal < 2 * notGradTotal:
                multiplier += 5
        # check pairing
        for pair in (('CS101', 'CS191'), ('CS201', 'CS291')):
            for section in ('A', 'B'):
                for section2 in ('A', 'B'):
                    class1, class2 = pair
                    class1 += section
                    class2 += section2
                    # if same time
                    for time in times:
                        if uniques.get((class1, time)) is not None and uniques.get((class2, time)) is not None:
                            multiplier -= 10
                    # if adjacent
                    for i in range(1, len(times)):
                        time1 = times[i-1]
                        time2 = times[i]
                        if (uniques.get((class1, times[i])) is not None and uniques.get((class2, times[i-1])) is not None) or (uniques.get((class2, times[i])) is not None and uniques.get((class1, times[i-1])) is not None):
                            multiplier += 5
                            if (uniques.get((class1, times[i])) is not None and uniques.get((class2, times[i-1])) is not None):
                                time1, time2 = time2, time1
                            # if same building
                            for room in rooms:
                                for room2 in rooms:
                                    if room == room2 or (room[:4] == 'HAAG' and room2[:4] == 'HAAG') or (room[:9] == 'FLARSHEIM' and room2[:9] == 'FLARSHEIM'):
                                        if uniques.get((class1, room, time1)) is not None and uniques.get((class2, room, time2)) is not None:
                                            fitness_value += 5
                                    if room.startswith('KATZ') ^ room2.startswith('KATZ'):
                                        multiplier -= 3
                                    if room.startswith('BLOCH') ^ room2.startswith('BLOCH'):
                                        multiplier -= 3
        

        fitness_value *= multiplier / 100
        return fitness_value
