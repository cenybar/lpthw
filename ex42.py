# ex42.py

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a object
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## Cat is-a object
class Cat(Animal):
    def __init__(self, name):
    ## ??
        self.name = name

## ??
class Person(object):
    def __init__(self, name):
    ## Person has-a name of some kind
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a object
class Employee(Person):
    def __init__(self, name, salary):
        ##  hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Empoyee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass
## Salmon is-a object
class Salmon(Fish):
    pass
## Halibu is-a fish object
class Halibut(Fish):
    pass
## rover is-a Dog
rover = Dog("Rover")
## satan is-a Cat
satan = Cat("Satan")
## mary is-a PErson 
mary = Person("Mary")
## mary has-a pet
mary.pet = satan
## frank is-a employee
frank = Employee("Frank", 120000)
## frank has-a pet
frank.pet = rover
## filpper is-a Fish
flipper = Fish()
## crouse is-a Salmon
crouse = Salmon()
## harry is-a Halibut
harry = Halibut()