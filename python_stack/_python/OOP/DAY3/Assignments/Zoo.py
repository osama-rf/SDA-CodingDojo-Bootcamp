class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append( Lion(name) )
        return self

    def add_tiger(self, name):
        self.animals.append( Tiger(name) )
        return self

    def add_panda(self, name):
        self.animals.append( Panda(name) )
        return self

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
        return self

    def feed_all(self):
        for animal in self.animals:
            animal.feed()
        return self


class Lion(Zoo):
    def __init__(self,name,health_level = 6 ,happiness_level = 7, age = "unknown"):
        self.name = name
        self.age = age
        self.health = health_level
        self.happiness = happiness_level
    
    def display_info(self):
        print(
            f"Name: {self.name}",
            f"Type: {type(self).__name__}",
            f"Age: {self.age}",
            f"Heath: {self.health}",
            f"Happiness: {self.happiness}",
            sep="\n" , end="\n\n")
        return self
    
    def feed(self):
        self.health += 10
        self.happiness += 10
        return self

class Tiger(Zoo):
    def __init__(self,name,health_level = 8 ,happiness_level = 5, age = "unknown"):
        self.name = name
        self.age = age
        self.health = health_level
        self.happiness = happiness_level
    
    def display_info(self):
        print(
            f"Name: {self.name}",
            f"Type: {type(self).__name__}",
            f"Age: {self.age}",
            f"Heath: {self.health}",
            f"Happiness: {self.happiness}",
            sep="\n" , end="\n\n")
        return self
    
    def feed(self):
        self.health += 10
        self.happiness += 10
        return self

class Panda(Zoo):
    def __init__(self,name,health_level = 8 ,happiness_level = 10, age = "unknown"):
        self.name = name
        self.age = age
        self.health = health_level
        self.happiness = happiness_level
    
    def display_info(self):
        print(
            f"Name: {self.name}",
            f"Type: {type(self).__name__}",
            f"Age: {self.age}",
            f"Heath: {self.health}",
            f"Happiness: {self.happiness}",
            sep="\n",end="\n\n")
        return self

    def feed(self):
        self.health += 10
        self.happiness += 10
        return self

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala").add_panda("Kruf").add_lion("Simba").add_tiger("Rajah").add_tiger("Shere Khan").print_all_info()
zoo1.animals[0].display_info().feed().display_info()