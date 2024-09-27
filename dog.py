class Animal():
    def __init__(self, name:str, age: int):
        self.name = name
        self.age = age
    def describe(self):
        print("This is", self.name, "it has", self.age, "years old")

class Dog(Animal):
    def __init__(self, name:str, age:int,breed):
        super().__init__(name,age)
    def bark():
        print("Woof-woof")

knopa = Dog("Knopa", 5, "mongrel")
knopa.bark()