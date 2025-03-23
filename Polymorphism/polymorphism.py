
# Polymorphism : Many form of a particular element
class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self): 
        return "Meow"
    super().make_sound()

# Polymorphism: Using the same method name across different classes
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.make_sound())
