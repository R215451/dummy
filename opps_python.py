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


class A:
    def display(self):
        print("abc")  # Only this print statement will execute

class B(A):
    def display(self):
        super().display()  # Calls display method in class A

class C(B):
    def display(self):
        super().display()  # Calls display method in class B

# Instantiate the C class and call its display method
c_instance = C()
c_instance.display()

class StudentData:
    def __init__(self,name):
        self.name = name
class StudentRollNumber(StudentData):
    def __init__(self, name,roll_number):
        super().__init__(name)
        self.roll_number = roll_number

student = StudentRollNumber('Moise','77')
print(student.name)
print(student.roll_number)

