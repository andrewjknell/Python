class Animal:
    def __init__(self, name, age):
        self.name = name 
        self.age = ('age '+(str(age)))
        self.health = 10
        self.happiness = 10
        self.zoo_animals = []

    def feed(self,amount):
        self.health += (amount/10)
    
        

class Monkey(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def display_all(self):
        print(self.name)
        print(self.age)

class Lion(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = ('speed '+(str(speed) + 'mph'))
    def display_all(self):
        print(self.name)
        print(self.age)
        print(self.speed)
class Penguin:
    def __init__(self, name):
        self.name = 'penguin'



