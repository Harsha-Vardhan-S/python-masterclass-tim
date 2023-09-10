# There's no difference between single or double quotes in Python.
# However, if you start a string with one type then you must finish it with the same type
print("Today is a good day to learn Python")
print('Python is fun')

# If you need to include a single quote within the string then use double quote to enclose the string and vice-versa
print("Python's string are easy to use")
print('We can even include "quotes" in strings')

# String concatenation
print("hello" + " world")

# Binding string values to variables
greeting = "Hello"
name = "Harsha"

print(greeting + name)

# If we want a space, we can add that too by enclosing space between quotes as a string
print(greeting + ' ' + name)

# Using input function to take text input from the keyboard
# Assignment is done using the equals symbol and anything on the right of the equals symbol is evaluated first
# before the assignment happens. Here in our case input function is called first.
# The value the input function returns upon the user input is assigned to the variable name
name = input("Please enter your name ")
print(greeting + ' ' + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

age = "2 years"
print(age)
print(type(age))