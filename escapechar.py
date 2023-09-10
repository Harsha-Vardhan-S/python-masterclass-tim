# "\" Escape Character (BACKSLASH Character) is used to escape the character that follows it, to give a special meaning
# \n To start a new line
splitString = "This string has been\nsplit over \nseveral \nlines"
print(splitString)
print()
# \t To insert tab stops in the same line. Different consoles have different tab stops
# In intellij idea tab stops for every 4 characters.
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)
print()
# Backslash can also be used to escape special characters such as single quote or double quote
# if a string contains both of those characters, if we delimit the string using single quotes,
# then we have to escape any single quotes that appear inside the string
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
print()
# (or)
# if we delimit the string using double quotes, then we have to escape any double quotes that appear inside the string
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
print()
# When using Triple Quotes (""" """), then there is No Need To Escape Any Quotes Inside The String.
# Python knows that the string doesn't end, until it finds those matching Triple Quotes at the end.
print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")
print()
# Python allows use of Triple Quotes (""" """) to split a string over several lines without the use of "\n"s.
# This feature allows for a more readable code.
# The string on line 3, that we split earlier is not easy to read because of the embedded '\n's.

anotherSplitString = """This string has been
split over
several
lines"""
print(anotherSplitString)
print()
# If you want to lay out a string with line breaks while coding for sake of readability, but don't want linebreaks
# when printed to the console, then we can ESCAPE the end of the line with a BACKSLASH character.
anotherSplitString = """This string has been \
split over \
several \
lines"""
print(anotherSplitString)
print()

# What if you want to include BACKSLASH Character inside your string?
# Say you wanted to print the following string to console: C:\Users\timHarsha\notes.txt

# print("C:\Users\timHarsha\notes.txt")
# Because of the BACKSLASH Character, The IDE is interpreting the t in timHarsha as TabStop, n in notes.txt as LineFeed,
# U in Users as accented characters inside the string. So we CAN'T just include BACKSLASH Character by just typing
# inside the string.
# We can include the BACKSLASH Character inside a string using 2 methods.

# Method 1: Escape the backslash by putting another backslash before \ (Recommended)
print("C:\\Users\\timHarsha\\notes.txt")
print()
# Method 2: Using Raw string. We can create a Raw string by PREFIXING a string with letter r
print(r"C:\Users\timHarsha\notes.txt")