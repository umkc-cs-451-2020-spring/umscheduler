import random
from copy import copy
from typing import Union, List, Callable

class Gene(object):
    '''The basic unit of genetic algorithms, holding a value given from an enumeration of options.'''
    def __init__(self, name: str, value, boundary: int = None):
        self.name = name
        self.value = value
        # If mutated, make sure it's still in a valid state.
        self.boundary = boundary or self.value

    def raw(self) -> int:
        return self.value

    def binary(self) -> bin:
        return bin(self.value)

class MutableGene(Gene):
    '''A Gene that has the ability to mutate.'''
    def __init__(self, name: str, value, boundary: int = None):
        super().__init__(name, value, boundary)
    
    @staticmethod
    def mutable(self) -> bool:
        return True

    def mutate(self) -> type:
        self.value = random.randrange(self.boundary)
        return self
    
    def mutated(self) -> type:
        return copy(self).mutate()

class ImmutableGene(Gene):
    '''A Gene that is guaranteed not to mutate.'''
    def __init__(self, name: str, value, boundary: int = None):
        super().__init__(name, value, boundary)
    
    @staticmethod
    def mutable(self) -> bool:
        return False

class Allele(object):
    '''A enumeration of genotypical values that produces genes.'''
    def __init__(self, name: str, genotypes: list):
        self.name = name
        if not genotypes:
            raise IndexError('Allele genotypes not provided')
        # always convert iterable to list
        self.genotypes = [*genotypes]
        self.GeneType = Gene

    def __len__(self):
        return len(self.genotypes)

    def generate(self) -> 'self.GeneType':
        val = self.generate_raw()
        return self.GeneType(self.name, val, len(self))

    def generate_raw(self) -> tuple:
        return random.choice(range(len(self)))

    def __getitem__(self, i: int):
        # if a gene wants to retrieve its original value
        return self.genotypes[i]
    
class MutableAllele(Allele):
    '''An Allele that produces MutableGenes.'''
    def __init__(self, name: str, genotypes: list):
        super().__init__(name, genotypes)
        self.GeneType = MutableGene

class ImmutableAllele(Allele):
    '''An Allele that produces ImmutableGenes.'''
    def __init__(self, name: str, genotypes: list):
        super().__init__(name, genotypes)
        # indexing to prevent duplicates during one iteration
        self.current = 0
        self.GeneType = ImmutableGene
    def generate_raw(self) -> tuple:
        curr = self.current
        # bounding checks
        self.current += 1
        self.current %= len(self.genotypes)
        return curr