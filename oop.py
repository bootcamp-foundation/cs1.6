class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."


p1 = Person('ali', 19)
p2 = Person('vali', 13)
p3 = Person('john', 11)

persons = [p1, p2, p3]
oldest = max(persons, key=lambda person: person.age)

print(oldest)
