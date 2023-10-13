# 35. String Operators
print(("-" * 20) + "35. String Operators" + ("-" * 20) + "\n")
# In this video, we will look at three operators that apply to strings. In fact, they apply to any Sequence type.
# Python 3 has 5 Sequence types built-in:
#       1.String type
#       2.List
#       3.Tuple
#       4.Range
#       5.Bytes and ByteArray (which I’m treating sort of as 1 Sequence type)
#
# What is the Sequence?
# A Sequence is defined as an ordered set of items.
# For example, the string “Hello World” contains 11 items, and each item is a character.
# But a List is also a Sequence type. For example, here’s a Python List of things you might need when buying a computer.
# [“computer”, “monitor”, “keyboard”, “mouse”, “mouse mat”]

# You can see that each item is in a double quote, separated by a comma, and it’s all then in left and right square
# brackets. So that List contains five items, each of which is a String.
# You’ll be looking at Lists in the later section of this course.

# *That last example was a List of strings. In other words, it’s a Sequence where each item is also a Sequence.
# *Make sure you fully understand the videos on Indexing, because Indexing is very important when dealing with Sequences

# ***Because a Sequence is “Ordered”, we can use indexes to Access individual items in the Sequence.
# For example below, we have computer_parts defining a List:
# computer_parts = [“computer”, “monitor”, “keyboard”, “mouse”, “mouse mat”]
# Then 
# computer_parts[1]     # monitor
# will be the string “monitor”, which is the 2nd entry in the List.
#
# But that’s also a Sequence, and we can index into that Sequence as well:
# computer_parts[1][0]      # m
# by using [1] to get access to monitor. Then [0] would be the letter “m” in lower case, which is the first part of
# that Sequence.

# We’ve been looking at Strings in this section, but everything that you can do with the String Sequence type can also
# be done with the other Sequence types.
# Well, everything with One Exception. Not all Sequence types can be concatenated or multiplied. Range is an example of
# a Sequence that can’t be concatenated

# Create a new Python file called sequence_operators
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)      # he's probably pining for the fjords
print()
# But the + Plus operator isn’t necessary when concatenating string literals, in Python.
# So we can also print the same output by writing the code as follows:
print("he's " "probably " "pining " "for the " "fjords")    # he's probably pining for the fjords
print()

# If you run this, we should see both line 47, 51 outputting the identical output.
# So I mentioned this second way on line 51, because it’s how Python works, not because we think you’d ever want to do
# something like that. I’m sure you’d agree that the first example on 47 is a bit easy to read.
print("he's", "probably", "pining", "for the", "fjords")  # he's probably pining for the fjords
# Using , (Comma) between string literals automatically introduces space between string literals in output.
print()

# Strings can also be multiplied, which is a bit weird if you come from another programming language.
print("Hello " * 5)     # Hello Hello Hello Hello Hello
print()
# You can’t actually perform arithmetic Multiplication on strings, of course.
# Instead, what happens is the * (multiplication operator) Repeats the Sequence a certain number of times,5 in this case
# Lists and Tuples can also be multiplied as we'll see when we look at those sequence types later in the course.
# You can’t concatenate or multiply a Range though, and that’s not a problem, because you probably wouldn’t want to do
# that anyway.

# Now, once again, operator precedence applies here as well

# print("Hello " * 5 + 4)     # TypeError: can only concatenate str (not "int") to str
# This example wouldn’t print “Hello”, 9 times. Again, we’re talking about operator precedence here.
# So if we’ve run this program, we see that we get an TypeError.
# The reason we’re getting the error is that Hello in double quotes, multiplied by 5 evaluates to a string, and then
# there’s an attempt to add the numeric number 4 to it, and it Fails for that reason.

# We can actually do two different things here.
print("Hello " * (5 + 4))       # Hello Hello Hello Hello Hello Hello Hello Hello Hello
print()
# Because of the parenthesis, line 80 evaluates 5 + 4 to get 9. So it should then repeat the string Hello, 9 times.

print("Hello " * 5 + "4")       # Hello Hello Hello Hello Hello 4
print()
# Line 84 should repeat the string Hello 5 times, and then append the string 4 to it.

# ***There’s also an operator to CHECK if one string is a substring of another.
# To do that, we actually Check if one thing is in another.
# So let’s start by typing some code
today = "friday"
print("day" in today)           # True
print("fri" in today)           # True
print("thur" in today)          # False
print("parrot" in "fjord")      # False
print()
# So here, the “in” operator evaluates to true if the first thing exists in the 2nd and false otherwise. We’ll be using
# that a lot when we look at Conditions and For loops, and you’ll get plenty of practice using it and see loads of real
# examples.

# +, *, in, operators
print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")
# -----------------------------------------------
