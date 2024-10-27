class Dog:
    def __init__(self,name,breed):
        self.name  = name
        self.breed = breed

    def display_info(self):
        return f"{self.name} is a {self.breed}"
    
    def bark(self):
        return "Woof!"

my_dog = Dog('Buddy','Golden Retriever')
print(my_dog.display_info())
print(my_dog.bark()) 


class Animal:
    def speak(self):
     return 'Animal speaks'
class Cat(Animal):
    def speak(self):
        return 'Cat Meow' 
cat = Cat()
print(cat.speak())    