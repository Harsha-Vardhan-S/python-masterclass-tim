# 54. in and not in             Part-1

print(("-" * 20) + "54. in and not in" + ("-" * 20) + "\n")

# > Before we finish with conditions, I want to look now at “in” and “not in”.
# > There are two uses of “in” and we’re going to be seeing it used with a “for” Loop later. Here though, we’re
# concentrating on using “in” as a Condition.
# > Create a new Python file checkingin.py
# *** “in” is used in sequences, and we will make much more use of it when we come to look at LISTS in a later section
# in the course.
# One sequence that we have used though is a String, a Sequence of Characters.
# Let’s type in some code:

parrot = "Norwegian Blue"

letter = input("Enter a character: ")                       # Enter a character: a

if letter in parrot:
    print("{} is in {}".format(letter, parrot))       # a is in Norwegian Blue
else:
    print("I don't need that letter")

# > I am gonna start by entering the letter “a” when asked for character here.
# > So that assigns the name letter to string value “a” and line 5 checks if the letter appeared in the parrot string.
# > It does appear in Norwegian blue, so their condition evaluates to True, and we get the message, “a is in Norwegian
# Blue” printed out.

# We’ve got to run the program again. This time I’m going to try a letter that doesn’t appear in the string.

parrot = "Norwegian Blue"

letter = input("Enter a character: ")                       # Enter a character: z

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")                       # I don't need that letter

# So, I’m going to enter letter “z”. We got the output, I don’t need that letter
# *** When you enter the input, Remember that String Comparisons are case-sensitive. If you enter a capital A, it
# won’t be found in the string.


# You can also check for longer sequences.
# Let’s run the program again.

parrot = "Norwegian Blue"

letter = input("Enter a character: ")                       # Enter a character: Blue

if letter in parrot:
    print("{} is in {}".format(letter, parrot))       # Blue is in Norwegian Blue
else:
    print("I don't need that letter")

# I’m going to enter Blue with a capital B, and press enter. We got the output, Blue is in Norwegian Blue

# If you try that with blue, all in lowercase, it won’t be found
parrot = "Norwegian Blue"

letter = input("Enter a character: ")                       # Enter a character: blue

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")                       # I don't need that letter

#
