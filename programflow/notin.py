# 54. in and not in             Part-2
print(("-" * 20) + "54. in and not in Part-2" + ("-" * 20) + "\n")

# As well as checking if something is “in” a Sequence, we can test if it isn’t, and we do that using “not in”.

activity = input("What would you like to do today? ")       # I want to learn Python

if "cinema" not in activity:
    print("But I want to go to the cinema")                 # But I want to go to the cinema

# > If you run this program now and I’m going to type, I want to learn Python
# > We got the output, But I want to go to the cinema. Because the string “cinema” isn’t in the inputted string, “I want
# to learn Python”, the Boolean expression evaluates the True. Remember that we’re using “not in” here.
# *** String comparisons are Case-Sensitive, and this can cause way confusion for our Users if we don’t handle it
# correctly.

# To see what I mean. I’m going to run the program again
activity = input("What would you like to do today? ")       # I want to go to the Cinema

if "cinema" not in activity:
    print("But I want to go to the cinema")                 # But I want to go to the cinema

# > I’m going to enter the text, I want to go to the Cinema. Here I have used a capital C for Cinema and, we still get
# the message, But I want to go to the cinema.
# > Now that could be a bit confusing, for Users of your programs. Fortunately, though, that’s an easy thing to deal
# with. Python strings have a load of useful functions, and one of them Converts a String to lowercase. In fact, there
# are 2 functions that do a similar thing.

# > I’ll show you how to find them all in a moment. But firstly, let us modify our program slightly.
# *** We are going to use the .casefold() function on line 40
# > The casefold() function CONVERTS a string to lowercase, but it handles different character sets BETTER than just
# converting to lowercase() function would. Unless you’re familiar with languages like German, they have different
# lowercase representations of some letters, you probably wouldn’t be aware of the problem.
# *** Just remember to use the casefold() function rather than the lowercase() function when you want to
# Compare Strings
# Lets run the program

activity = input("What would you like to do today? ")       # What would you like to do today? I want to go the Cinema

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")

# > We are going to type, I want to go the Cinema, with a capital C.
# > We don’t get that confusing message anymore, because the match has now clearly worked using the casefold() function.

# > I’m going to finish this video by having a look at all the functions that the Python string class provides.
# Link: https://docs.python.org/3/library/stdtypes.html#string-methods

# > Now, I wouldn’t suggest trying to memorize all these methods, but it is worth spending some time reading about them.
# When you need to do something, such as checking if a string contains only digits, for example, you’ll remember that
# there’s a method to do that. You won’t remember what it’s called unless you’ve used it a few times, but you’ll know
# where to go to find it. We’ll be using quite a few of these methods throughout the course, so you’ll get a lot of
# practice at using them.
# > We’ve covered quite a bit about “if” statements and conditions. Before we move on to start looking at Loops, the
# next video is going to be a challenge to let you practice some of what you’ve learned so far. See you in the next
# video.
print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")
# ----------------------------------------------------------------------------------------------------------------------
# Challenge:

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if 18 <= age < 30:
    print("Welcome to the holiday")
else:
    print("Sorry, You age is not appropriate for entry")
