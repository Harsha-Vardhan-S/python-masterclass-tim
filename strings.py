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

# If we want a space, we can add that too by delimiting space between quotes as a string
print(greeting + ' ' + name)

# Using input function to take text input from the keyboard
# Assignment is done using the equals symbol and anything on the right of the equals symbol is evaluated first
# before the assignment happens. Here in our case input function is called first.
# The value the input function returns upon the user input is assigned (bound) to the variable name
name = input("Please enter your name ")
print(greeting + ' ' + name)
print()

'''Few Rules for Variable Names:
1.	Python variable names MUST begin with the letter, either upper or lowercase, or an _ underscore character.
2.	They can contain letters, numbers, or underscore characters. However, they Can’t Begin With A Number.
3.	Python variables are Case-Sensitive. So greeting with a lowercase g and Greeting with an uppercase G would refer to two different variables.
4.	Variables are created when they are first attached to a value, using the  = '''

# We shall create another variable age and bind (attach) it to the value 24
age = 24
print(age)

# Python is dynamically and strongly typed language.
# data type describes the kind of information that we are storing.
# There are a number of data types built into python. We’ve already seen the String and Integer types.
# Greeting is a string type and age is an int. But you don’t have to take my word for that.
# We can ask python what type it thinks they are.

print(type(greeting))
print(type(age))
print()
# In Python, we can Rebind a variable to value of different data type.
# That wouldn’t be possible in many other languages. Once the variable has a type, you can only assign values of
# that type to it. Java and C your examples of languages that behave in that fashion.
# Hence,  in Python it can be more useful to think of the value as having the data type than the variable.

age = "2 years"
print(age)
# Here, variable age is now bound to a string value. It’s no longer an int.
# We have Rebound the variable(label) age to the string value 2 years
print(type(age))