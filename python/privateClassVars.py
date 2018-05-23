class Animal(object):
    __name = "" # private variable

    def __init__(self, name):
        self.__name = name

    def printName(self):
        print(self.__name)

myAnimal = Animal("Fluffy")
myAnimal.printName()


print("")

class Animal2(object):
    name = "" # this can be accessed by the user

    def __init__(self, name):
        self.name = name

    def printName(self):
        print(self.name)

myAnimal = Animal2("Fluffy2")
myAnimal.printName()
print(myAnimal.name)

print("")

# private functions

class Animal3(object):
    name = ""

    def __init__(self, name):
        self.name = name

    def __printName(self):
        print(self.name)

myAnimal = Animal3("Fluffy3")
print(myAnimal.name)
myAnimal.__printName()

