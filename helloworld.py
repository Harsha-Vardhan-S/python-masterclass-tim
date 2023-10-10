# 17. Our First Python Program
print('Hello, World!')      # Hello, World!
# Although it’s very simple, our helloworld program does include a few important basics.
# Firstly, we’ve used the Python function print()
# Python has many functions, such as mathematical functions like round() to round the number of digits after the
# decimal point and char(), ord() to convert characters to numeric representations, and vice versa, as well as many more
# You can also define your own functions, as we’ll see later in the next video. We’ll see more ways to use the
# print() function.
print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")  # --------------------End of Topic--------------------

# --------------------------------------------------------------------------------

# 18. Printing in Python

print('Hello, World!')      # Hello, World!
# Now, we’ve got a very simple program that just prints out the text: Hello, World!
# There are a few important things to know about the code, and I’ve already mentioned that print() is a function.
# When you call a function in Python, you provide the things you want to print inside ( ) parentheses. So we have
# provided a string literal, Hello, World!,  and that’s what got printed.
# A String Literal is a sequence of characters, anything you can type on the keyboard basically enclosed in quotes.
# You can use either a ‘ ’(single quotes) or “ ” (double quotes) to enclose a string.
# I used ‘ ’(single quotes), but you could use “ ” (double quotes) if you wanted to.
# ***It’s important though, to use the same ones. So if you start a string with “ (double quote), it has to be
# terminated with a ” (double quote).

# print('Hello, World!")
# So, if I change my ’ (single quote), at the end of Hello, World!, to a ” (double quote), suddenly we’ve got an error
# there. You can’t start with a single quote and end with the other. You must use the same type at the start and at the
# end.

# The string literal, “Hello, World!” is called an Argument, at least in the context of what we’re doing here. We’re
# passing the argument to the print() function.
# Functions can take more than one argument, and we’ll be looking at how to define those when we write our own
# functions later in the course
# So we’re passing a string argument to the print() function, but we could also print, for example, the result of
# calculations.

# Let’s go ahead and add some calculations.

print(1 + 2)        # 3
print(7 * 6)        # 42
print()
# Now printing with left and right parentheses without telling Python what to print, just produces a blank line.
# You can see that blank line in output. We still need the () parenthesis, even though we’re not providing an argument.

# ***When calling a function, you must have a () parenthesis after the function name.

print("The end")        # The end
print()

# Functions often take a specific number of arguments, but it’s also possible to write functions that can take a
# variable number of arguments. The print() function that’s built into Python has been written that way. What that means
# is we can print several things at once.

# So let’s change the code on line 48 to print several strings and a number.
print("The end", "or is it?", "keep watching to learn more about Python", 3)
# Output: The end or is it? keep watching to learn more about Python 3

# When we run the program, you can see now that we’ve got three strings and a number printed on that output.
# So, each argument is separated from the previous one with a comma in the code on line 52. We’re passing 4 arguments
# on this line to print.
# So, the first argument is “The end”, and that’s followed by a comma to separate it from the 2nd argument,
# “or is it?” Once again, we need a comma before we provide the 3rd argument, “Keep watching to learn more about python”
# and the final argument is the numeric literal 3 which is also separated from the previous argument with a comma.

# There are still a few more things to learn about the print() function, and we will be coming back to it in later
# videos. For now, we’ve learned enough to be able to print from our programs to cheque that they produce the correct
# results.
print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")  # --------------------End of Topic--------------------

# Now I’ve introduced quite a few jargon words there, so let’s finish this video with a slide to summarise them.

# Literal: A value of some type.
# Examples of numeric literals are: 1, 42, and 98.04
# Examples of a string literals are: “Hello, World!”, “Guido Van Rossum”, “Python”

# function: A named block of code that we can call, by using its name.
# We can write our own functions, or we can use functions that are built into Python (such as what print() function.
# In Python, all functions return a value.

# Argument: A value is passed to a function in order to give it values to work with.
# There may be No Arguments, or there may be One Or More.
# Arguments appear in parentheses after the function name.
# If there are no arguments, you still have to type in the left and right parentheses.

# Calling a function: Using the function name to execute the function’s code.
# When you call a function, you have to provide the arguments that the function expects.
# If it doesn’t expect any arguments, don’t put anything between the parentheses.

# Return value: The value that a function returns.
# We haven’t talked about that yet, but it belongs in this slide to make the slide complete.

# Parameter: Also called formal parameter.
# This is something else we haven’t discussed yet, and we’ll learn about parameters when we start writing our own
# functions.
# ------------------------------------------------------------------------------------------------------------

# Coding Exercise 1: Printing text

# Write the code to print out the string: My hovercraft is full of eels

print("My hovercraft is full of eels")      # My hovercraft is full of eels

print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")  # --------------------End of Topic--------------------

# ------------------------------------------------------------------------------------------------------------
# Coding Exercise 2: Printing the result of a calculation
# Write a program to print the answer to the calculation 6 times 7
print(6 * 7)        # 42

print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")  # --------------------End of Topic--------------------
