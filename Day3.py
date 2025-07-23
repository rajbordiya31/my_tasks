# class Dog:
#     species = "canine"

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         # Create Objects
# d = Dog("Thunder",3)
# d1= Dog("Charlie",5)

# #Access Variables
# print(d.name) #instance variable
# print(d1.name) #Instance VAriable
# print(d.species) #Class Variable

# #Modify Instance Variable
# d1.name = "Max"
# print(d1.name)

# #Modify Class Variable
# Dog.species="Ferline"
# print(d.species)

# Access Attributes

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def show(self):
#         print(self.name)
#         print(self.salary)
# emp= Employee("Raj",25000)
# # print(emp.salary)
# # print(emp.name)

# # Access Attributes
# print(getattr(emp, 'name')) 

# # Check attribute existence
# print(hasattr(emp, 'salary'))

# # Dynamically add a new attribute
# setattr(emp, 'age', 30)  
# print(getattr(emp, 'age')) 

# # Delete an instance attribute
# delattr(emp, 'salary') 
# print(hasattr(emp, 'salary'))

# Accessing Methods

# class Employee:
#     def __init__(self,name,salary,category):
#         self.name=name
#         self.salary=salary
#         self.category=category

#     def show(self):
#         return f"Name : {self.name}, salary : {self.salary}"
    
#     def cat(self):
#         return f"minimum salary :{self.category}"
    
# emp= Employee("Raj",25000,"min category")


# if hasattr(emp, 'show'):
#     print("method exists")
#     print(getattr(emp, 'show')())

# setattr(emp, 'cat', lambda: f'New method output: salary : {emp.category}')
# print(getattr(emp, 'cat')())


# class Parent:
#     def __init__(self):
#         self.parrent_attr = "Parent Class"
#     def show(self):
#         print(self.parrent_attr)

# class Child(Parent):
#     def __init__(self):
#         super().__init__()  
#         self.child_attr = "Child Class"
    
#     def display(self):
#         self.show()  
#         print(self.child_attr)

# child = Child()
# child.display()


# Default Constructor

# class Car:
#     def __init__(self):
#         self.make="Toyota"
#         self.year=2020
#         self.model="Fortuner"
# car=Car()
# print(car.make)
# print(car.model)
# print(car.year)

#Parameterized Constructor
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.year=year
        self.model=model
car=Car("Toyota","Fortuner",2020)
print(car.make)
print(car.model)
print(car.year)
        

    
   
  
    
        