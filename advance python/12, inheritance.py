# Inheritance allows one class (child/derived class) to acquire properties and methods of another class (parent/base class).
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()   # Inherited method
d.bark()
