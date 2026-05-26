# Create constructor using __init__().
class person :
    def __init__(self,name, age):
        self.name = name
        self.age = age
person = person("tanny", 21)
print(person.name)
print(person.age)
