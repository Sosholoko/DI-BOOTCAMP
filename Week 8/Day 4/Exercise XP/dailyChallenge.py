import random

class Gene:
    def __init__(self, value=0):
        self.value = value

    def flip(self):
        if self.value == 1:
            self.value = 0
        else:
            self.value = 1



class Chromosome:
    def __init__(self, genes):
        self.genes = genes

    def mutate(self):
        for gene in self.genes:
            if random.randint(0,1) == 0:
                gene.flip()


class DNA:
    def __init__(self, chromosomes):
        self.chromosomes = chromosomes

    


def get_random_chr():
    
    genes = []
    
    i = 0
    while i <= 10:
        gene = Gene(random?randit(0,1))
        genes.append(gene)

        i += 1

    chromosome = Chromosome(genes)
    return chromosome



chromosomes = []


# genes = [Gene(), Gene(1),Gene(), Gene(1),Gene(), Gene(1),Gene(), Gene(),Gene(1), Gene()]
# chromosome = Chromosome(genes)

i = 0
while i <= 10:
    
    genes = []
    i2 = 0
    while i2 <= 10:
        gene = Gene(random?randit(0,1))
        genes.append(gene)

    i2 += 1

    chromosomes = Chromosome(genes)
    chromosomes.append(chromosome)

    i += 1