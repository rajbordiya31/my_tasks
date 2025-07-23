# Variables :- There is no command to declare a variable. variable is automatically created when we assign a value to it

# x=5
# y="Raj"
# print(type(x))
# print(type(y))

# Input and output operations

# w=input("Enter the number =")

# print(w)
# print(type(w)) #this is string type because input default string hi hota hai

# #After type casting
# x=int(input("Enter the number :"))
# print(x)
# print(type(x)) #after type casting int type

# Output Formatting
#  using sep and end parameter

# print("Raj" ,end="@")
# print("gmail.com")

# print("Raj","gmail.com",sep="@")
# print('22','7','2025',sep="-")

# # USING f String
# name = input("Enter your Name : ")
# age = int(input("Enter your age : "))
# print(name)
# print(age)
# print(f"My name is {name} and I am {age} years old.Ra")


# If else

# x= int(input("Enter the age : "))
# if x>18:
#     print("Eligible for driving")
# else:
#     print("Not Eligible")

# if elif else

x=int(input("Enter Number :"))
if x>0:
    print(f"The Number {x} is positive number.")
elif x<0:
    print(f"The Number {x} is negative number.")
else:
    print(f"The Number {x} is zero.")



