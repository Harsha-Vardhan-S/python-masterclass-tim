# 20. The Escape Character

# "\" (Escape Character or BACKSLASH Character) is used to Escape the Character that Follows it, to give that character
# a special meaning.
#   Ex1: \n to start a new line
#   Ex2: \t to insert a tab stop

# Lets create a new file escapechar.py

# \n To start a new line
splitString = "This string has been\nsplit over \nseveral \nlines"
print(splitString)
# Output:
# This string has been
# split over
# several
# lines

# Whenever the print() function sees \n in a string, it causes it to start a new line.
# You can see how the string has been indeed spit over several lines in the output.
# # Many ides will color Escape Characters differently in the code.
print()

# \t To insert tab stops in the same line. Different consoles have different tab stops
# In intellij idea tab stops for every 4 characters.
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)             #   1	2	3	4	5
print()

# Backslash can also be used to escape Special Characters such as ‘ ’ (single quotes) or “ ” (double quotes)
# Say, if a string contains both of those characters, and we have Delimited the string using ‘ ’ (single quotes), then
# we have to escape any ‘ ’ (single quotes) that appear inside the string using \ (backslash).
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# The pet shop owner said "No, no, 'e's uh,...he's resting".
print()

# (or)

# If we delimit the string using “ ” (double quotes), then we have to escape any “ ” (double quotes) that appear inside
# the string using \ (backslash).
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
# The pet shop owner said "No, no, 'e's uh,...he's resting".
print()

# When using Triple Quotes (""" """), then there is No Need To Escape Any Quotes Inside The String.
# Python knows that the string doesn't end, until it finds those matching """ (Triple Quotes) at the end.
print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")
# The pet shop owner said "No, no, 'e's uh,...he's resting".
print()

# Python allows use of Triple Quotes (""" """) to split a string over several lines without the use of "\n"s.
# This feature allows for a more readable code.
# The string on line 3, that we split earlier is not easy to read because of the embedded '\n's.

anotherSplitString = """This string has been
split over
several
lines"""
print(anotherSplitString)
# Output:
# This string has been
# split over
# several
# lines
print()

# If you want to lay out a string with line breaks while coding for sake of readability, but don't want linebreaks
# when printed to the console, then we can ESCAPE the end of the line with a BACKSLASH character.
anotherSplitString = """This string has been \
split over \
several \
lines"""
print(anotherSplitString)       # This string has been split over several lines
print()

print("""The pet shop owner said "No, no, \
'e's uh,...he's resting".""")       # The pet shop owner said "No, no, 'e's uh,...he's resting".
print()

print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")

# ------------------------------------------------------------------------------------------------------------
# Coding Exercise 3:
# Printing tabs
# Write a program that will produce the following output.  All the text should appear in your program's output.
#
# Output:
#   Number 1	The Larch
#   Number 2	The Horse Chestnut

print("Number 1\tThe Larch")
print("Number 2\tThe Horse Chestnut")
# Output:
#   Number 1	The Larch
#   Number 2	The Horse Chestnut
print()
print(("-" * 20) + "End of Coding Exercise" + ("-" * 20) + "\n")

# ----------------------------------------------------------------------------------------------------------------------
# 21. More on Escape Characters in Strings

# What if you want to include BACKSLASH Character inside your string?
# Say you wanted to print the following string to console: C:\Users\timHarsha\notes.txt

print("C:\Users\timHarsha\notes.txt")
# Because of the BACKSLASH Character, The IDE is interpreting the t in timHarsha as TabStop, n in notes.txt as LineFeed,
# U in Users as accented characters inside the string. So we CAN'T just include BACKSLASH Character by just typing
# inside the string.

# Tip: To Duplicate a line, press: Ctrl D

# We can include the BACKSLASH Character inside a string using 2 methods.

# Method 1: Escape the backslash by putting another backslash before \ (Recommended)
print("C:\\Users\\timHarsha\\notes.txt")    # C:\Users\timHarsha\notes.txt
print()
# Method 2: Using Raw string. We can create a Raw string by PREFIXING a string with letter r
print(r"C:\Users\timHarsha\notes.txt")      # C:\Users\timHarsha\notes.txt
print()
print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")
