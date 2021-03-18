# import random
# # To get a random number between a and b, just use random.randint(a,b)

# class Gene:
#     def __init__(self, value=0):
#         self.value = value

#     def flip(self):
#         if self.value == 1:
#             self.value = 0
#         else:
#             self.value = 1


# class Chromosome:
#     def __init__(self, genes):
#         """
#         :param genes: A list of 10 Gene objects
#         """
#         self.genes = genes

#     def mutate(self):
#         for gene in self.genes:
#             if random.randint(0,1) == 0: # 1/2 chance to be 0
#                 gene.flip()

#     @classmethod # Decorator
#     def get_random_chromosome(cls):
#         """
#         1) There is no 'self' parameter anymore
#         2) It's replaced by 'cls' parameter that contains the class itself (Chromosome)
#         :return:
#         """
#         genes = []  # The genes that compose the chromosome
#         i = 0
#         while i <= 10:  # Genes creator
#             gene = Gene(random.randint(0, 1))
#             genes.append(gene)

#             i += 1
#         # Instead of:
#         # chromosome = Chromosome(genes)
#         # Use:
#         chromosome = cls(genes)
#         return chromosome

# class DNA:
#     def __init__(self, chromosomes):
#         """

#         :param chromosomes: A list of 10 Chromosome objects
#         """
#         self.chromosomes = chromosomes

#     def mutate(self):
#         for chromosome in self.chromosomes:
#             if random.randint(0,1) == 0: # 1/2 chance to be 0
#                 chromosome.mutate()

    
#     @classmethod
#     def get_random_dna(cls):
#     chromosomes = []

#     i = 0
#     while i <= 10: #Chromosomes creator
#         chromosome = Chromosome.get_random_chromosome()
#         chromosomes.append(chromosome)
#         i += 1

#     dna = cls(chromosomes)
#     return dna


# class Organism:

#     def __init__(self, dnas, mutate_prob):
#         self.dnas = dnas
#         self.mutate_prob = mutate_prob

#     def mutate(self):
#         for dna in self.dnas:
#             if random.randint(0,100) <= self.mutate_prob:
#                 dna.mutate()

#     @classmethod
#     def get_random_organism(cls):
#         dnas = []
#         i = 0
#         while i <= 10: #DNA creator
#             dna = get_random_dna()
#             dnas.append(dna)
#             i+=1
#                                 # vvv random mutate_prob
#         organism = Organism(dna, random.randint(0,100))
#         return organism





# organism = get_random_organism()



# class LotteryTicket:

#     count = 0
#     golden_count = 0
#     def __init__(self):
        
#         LotteryTicket.count += 1
#         LotteryTicket.golden_count += 1
#         self.golden = False
#         if LotteryTicket.count == 5:
#             self.golden == True
#             LotteryTicket.count = 0
        
#         print("LotteryTicket.count is now : ", LotteryTicket.count)

#     # def golden(self):
#     #     if LotteryTicket.count > 4:
#     #         self.golden = True
#     #         print("Congratulation, you just got a golden ticket !")
#     #     else:
#     #         print(f"You're the {LotteryTicket.count}th buyer ")


# ticket1 = LotteryTicket()
# ticket2 = LotteryTicket()
# ticket3 = LotteryTicket()
# ticket4 = LotteryTicket()
# ticket5 = LotteryTicket()
# ticket6 = LotteryTicket()



#Dunder Methods


# class LotteryTicket:

#     bought_tickets = 0
#     golden_counter = 0

#     def __init__(self):

#         LotteryTicket.bought_tickets += 1
#         LotteryTicket.golden_counter += 1

#         self.golden = False
#         self.ticket_number = LotteryTicket.bought_tickets

#         if LotteryTicket.golden_counter == 5:
#             self.golden = True
#             LotteryTicket.golden_counter = 0

#     def __str__(self): #Overriding Object.__str__
#         return f"<Ticket No {self.ticket_number}>"

        

#     def __repr__(self):

#         if self.golden:
#             return f"<Golden Ticket No {self.ticket_number} "

#         return f"<Ticket No {self.ticket_number}>"
        


# # class Object --> Mother class of every class in python
# tickets = []
# i = 0
# while i < 50:
#     ticket = LotteryTicket()
#     tickets.append(ticket)
#     i += 1

# print(tickets[25])
# print(tickets)



class Champion:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.current_hp = 20
        self.attack_point = 3
        self.xp_count = 0
        self.xp_to_next_level = 10

    def get_level(self):
        return self.level
    
    def set_level(self):
        self.level = new
    
    def level_up(self):
        self.set_level(self.level + 1)
        self.max_life_point += 3
        self.attack_point += 1
        self.current_hp = self.max_life_point
        self.xp_count = 0

    @property #make a function acting like an attribute
    def speed(self):
        return 5*self.level

morty = Champion("Morty")

