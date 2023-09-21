class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# Create instances of different animals
dog = Dog()
cat = Cat()
duck = Duck()

# Store the animals in a list
animals = [dog, cat, duck]

# Use polymorphism to make the animals speak
for animal in animals:
    print(animal.speak())
