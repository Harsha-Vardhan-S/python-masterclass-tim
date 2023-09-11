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
3.	Python variables are Case-Sensitive. So greeting with a lowercase g and Greeting with an uppercase G would refer to 
two different variables.
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

# age = "2 years"
print(age)
# Here, variable age is now bound to a string value. It’s no longer an int.
# We have Rebound the variable(label) age to the string value 2 years
print(type(age))

# So firstly, on line 38 we’ve attached the variable age to an int value 24. Further on, down on line 55 we’ve
# reattached that same label to a string value 2 years. At that point variable age is now bound to the string 2 years.
# So Java and C programmers might jump to the conclusion that python is a weekly typed language and doesn’t care what
# data type variables are and that’s a natural assumption, if you think in terms of assigning a value to a variable.
# Looking at that way, it looks like we’ve assigned a string value to an int variable. Age represents an int on line 38
# but is given a string online 55.

# If we think in terms of binding a variable to a value, things make more sense. On line 38 age is attached to an int
# value 24.
# When we rebind the label age to a string value on line 55 we’re saying that we no longer want that label to
# refer to an int. We now want to use it to refer to the string value two years.
# Reusing a variable name like that probably isn’t a good idea. It can make your code confusing to read. What
# we probably should have done is bind a more meaningful label to the string, say, age_in_words '''

age_in_words = "2 years"

# But just because python allows you to reuse a variable name for a different purpose, that doesn’t mean it’s not
# strongly typed. As an example, let’s say what happens if we try to add an int to the string.'''
print(name + " is " + age + " years old")

# It gives a TypeError and line number of the error code. It also gives description for what the actual error was.
# TypeError: can only concatenate str (not "int") to str
# Python knows what to do if you use plus with three strings. It concatenates them, or with two numbers, it calculates
# their sum. However, it’s got no idea what you intend if you try to add a string and a number.
# Some languages, such as Java, will automatically convert the number to a string and concatenate. But python doesn’t do
# this, hence the TypeError.
# Automatic type conversion can be useful, but it can also be a source of Hard to Find Bugs and python tries to prevent
# you from introducing errors in this way.
# When python displays an error like the one above, it’s telling you that your code won’t work. It provides as much
# information as possible to help you figure out the cause of error.
# Errors may be frustrating, but you’ll learn a lot from getting errors like this and more importantly, working at how
# to fix them.

print(name + " is " + age_in_words + " years old")
