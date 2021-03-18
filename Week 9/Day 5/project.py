class Human():
    def __init__(self, idn, name, age, prio, blood):
        self.idn = idn
        self.name = name
        self.age = age
        self.prio = prio
        self.blood = blood


human_list = []
priority_list = []

class Queue(Human):
    
    def __init__(self, idn, name, age, prio, blood):
        self.idn = idn
        self.name = name
        self.age = age
        self.prio = prio
        self.blood = blood
        
        

    def add_person(self):
        if self.age > 60 or self.prio == True:
            print(f"{self.name} added to the Priority queue")
            priority_list.append(self.name)
            print(priority_list)
        else:
            print(f"{self.name} is not a priority person, he will be add but at the regular queue")
            human_list.append(self.name)
            print(human_list)

    def find_in_queue(self):
        if self.age > 60 or self.prio == True:
            print(f"{self.name} is at the position")
            print(priority_list.index(self.name))
        else:
            print(f"{self.name} is at the position")
            print(human_list.index(self.name))

    def swap(self, person):
        if self.age > 60 or self.prio == True:
            a, b = priority_list.index(self.name), priority_list.index(person.name)
            priority_list[b], priority_list[a] = priority_list[a], priority_list[b]
            print(priority_list)
        else:
            a, b = human_list.index(self.name), human_list.index(person.name)
            human_list[b], human_list[a] = human_list[a], human_list[b]
            print(human_list)

    def get_next(self):
        if self.age > 60 or self.prio == True:
            print(priority_list[0])
        else:
            print(human_list[0])






joe = Queue("1000", "Joe", 65, True, "O")
don = Queue("2000", "Don", 50, False, "AB")
george = Queue("3000", "George", 88, True, "B")
marc = Queue("4000", "Marc", 32, False, "A")

don.add_person()
marc.add_person()
george.add_person()
joe.add_person()
don.find_in_queue()
george.find_in_queue()
joe.find_in_queue()
joe.swap(george)
joe.find_in_queue()