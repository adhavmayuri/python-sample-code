from abc import ABC,abstractmethod
 
class Animal(ABC):
 
    #concrete method
    def sleep(self):
        print("Going to sleep in a while")

     #concrete method
    def eat(self):
        print("Start eating")
    
    @abstractmethod
    def sound(self):
        print("This function for defining the sound of any animal")
        pass
 
class Snake(Animal):
    def sound(self):
        print("I hiss")
 
class Dog(Animal):
    def sound(self):
        print("I bark")
 
class Lion(Animal):
    def sound(self):
        print("I roar")