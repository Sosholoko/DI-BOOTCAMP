class Car:
    def __init__(self, color, brand, travel):
        self.color = color
        self.brand = brand
        self.travel = travel

    def get_info(self):
        print(f"The car is manufactured by {self.brand} \nHer color is {self.color} \nShe travelled until now {self.travel} Km")

    def traveled(self, distance):
        print(f"The car travelled {distance} km")
        self.travel += distance


car_1 = Car("silver", "Kia", 28000)


car_1.traveled(8)
car_1.get_info()




