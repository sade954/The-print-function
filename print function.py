#Asking user for a few things with responses
name = input("What is your name? ")
color = input("What is yout favorite color? ")
age = int(input("How old are you today? "))

#Asking user for a few things with responses using the end character
print(name, end= " ")
print("is " + str(age) + " years old", end= " ")
print("and loves the color " + color + ".", end= " ")
