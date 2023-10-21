# 58. Stepping through a for loop
print(("-" * 20) + "58. Stepping through a for loop" + ("-" * 20) + "\n")

number = "9,223;372:036 854,775;807"
# So what I’m gonna do is start by binding a variable by name "seperators" to the variable "number"
seperators = number[1::4]
print(seperators)               # ,;: ,;
print()

# Now we can use the separators variable to split out the individual values. This is the interesting part
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])         # [9, 223, 372, 36, 854, 775, 807]
print()
# Now, I don’t expect that code on lines 337 and 338 to make sense. Again, I’m using it to demonstrate why extracting
# every third character from a string might be useful. As you work through the course, you’ll learn what this code is
# doing, and you’ll be able to write code like that for yourself.

# If we run this program, you can see the output is now showing us the 7 values that we’ve extracted from the string
# that we bound to the “number” variable on line 330. I think that’s pretty impressive when you consider it’s only a few
# lines of code. It’s very hard to come up with real-world examples when all we’ve covered so far in the course of
# variables, int, and strings, but hopefully, that demonstration has put the slice into a useful context.

# ---------------------------------------------------------------------------------------------------------------------

# > Back in the previous section, we used a Slice to extract all the delimiters from a list of numbers. I’m going to
# start reviewing that code. I’ve called this file SteppingThroughForLoop.py, and I’ll grab that code from that previous
# section.
# > We used a Slice that started at Index position 1 which is the first , (comma) then extracted every 4th character
# until it reached the end of the string. That worked, but it does rely on there being 3 digits in each of the numbers
# after the first , (comma). That’s probably fine if the data came from another computer program, but it’s not something
# we can rely on if it uses typing in those numbers by humans.
# > In that case, we should Examine each character in the number String, to check if it’s a digit or not. As we saw in
# the previous video, a “for” loop can be used to do that.
# > We’re going to iterate over number and append anything that isn’t a digit to the separators String.
# > Once we’ve seen the code working, we’ll step through it with a debugger, so we can see what it’s doing.
# > The first step is to initialize our separators variable. This is something that causes a lot of confusion, and I’m
# going to spend a minute discussing it, once we’ve seen the code working.

number = "9,223;372:036 854,775;807"
# We are binding an Empty String to seperators variable
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char
# Link to string methods: https://docs.python.org/3/library/stdtypes.html#str.isnumeric
print(seperators)
# Now we can use the separators variable to split out the individual values. This is the interesting part
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])         # [9, 223, 372, 36, 854, 775, 807]
print()

# > We have used another one of the String Methods here on line 44. I provided a link to the string methods, and we’ll
# be looking at few of them in our examples.
# > isnumeric will return True if the character is a number and False otherwise.
# > We want to add things that aren’t a digit, which is why the condition becomes:
#   if not char.isnumeric():
# > I’m going to run the program to make sure that it works.
# > The first thing we get printed out is the string containing all the separators. Now that was printed by the code
# on line 47
# > These strings are created by a “for” loop on lines 43 to 45.
# > Now we use that string of separators on line 10 to get the individual numbers. Once again, don’t worry about
# lines 10 and 11 at the moment. You’ll learn all about them later. At the moment, we’re just using them to show why
# we want to extract all the separators from the number.

# Q) Our program works, but how? We’ll set a breakpoint on the “for” loop on line 43, and let’s run the program in the
# debugger.

# > In the variables pane, we can see the value of number. So it’s a string containing 7 numbers, separated by various
# separator characters. Below that, we can see that the variable “separator” is currently bound to an “” (empty string).
# As I said, I’ll come back to that later. Now, when I step over the code, which we’ll do now, you can see the
# variable “char” on line 43 gets the first character from the string. That’s the digit 9. We’re about to test if it’s
# a digit. So I'm going to step over line 44 to do that. The character 9 does represent a number, so isnumeric()
# returns True. We’re checking for “not isnumeric()”, which is False, so therefore, the code on line 45 is skipped.

# > Now we’re back on line 43. I’m going to step over again. Char now gets the next character from number, which is
# a , (comma). A , (comma) obviously doesn’t represent a number and isnumeric should return False. Not False is True
# and we should get line 45 executed this time. Let’s step over to check that and that’s good. Line 45 is about to be
# executed.

# > When you’re using the debugger like this, always spend time working out what’s going to happen before it does.
# That’ll really help you to learn how to read code without ultimately having to run it in the debugger.

# separators is currently an empty string. Line 45 will append the value of char to it, which should result in
# separators becoming a string containing a , (comma). Let’s step over and see. In the variables pane, now separators
# is a , (comma)

# > So we’ve seen how char is getting each of the characters in turn and we really don’t need to keep watching line 43.
# We’ve also said that line 45 is only executed when we get a character that’s not numeric. So it’s line 45 that we’re
# really interested in here.

# > We can debug more efficiently by clearing the break point on line 43 and setting one on line 45 instead. When we’ve
# done that, we can use the button that looks like a typical video play icon, a vertical bar on a triangle. The
# button’s name is “resume program”, and what that will do is run our code at full speed until it hits our breakpoint.
# So I click that button now and the debugger executes the code for the 2 2 and 3 in number and char now contains
# a ; (semicolon) in variable pane. That’s obviously not numeric, and that’s why we’ve got our breakpoint hit on
# line 45. When I execute that line 45, by stepping over, we can see that the ; (semicolon) is appended to the
# separators.

# > In the variables pane, separators now has two characters, a , (comma) and a ; (semicolon).

# > Now it can be easy to see the values in the editor pane. This IDE shows them in grey. You can see it at the end
# of line 41. We’ve got a , (comma) and a ; (semicolon). We’ve also got the current value of char, at the end of
# line 43.

# > We’re going to resume the program again by clicking on the icon, and that ran past 3 7 and 2. char, as you can
# see, is now a : (colon), and line 45 will cause that to be appended to our separator string when I step over, which
# I’ll do now. You can see the : (colon) has been added to separators on line 41 now.

# > Next we should get a “ “ (space), before 8 5 4. So let’s resume and actually forgot about the space there. You can
# see that, obviously,

# > We had a “ “ (space) in the string, which is non-numeric. We’ve hit that. Therefore, a “ “ (space) should be added
# to our separator string by step over, which will do now, and you can see the string, the “ “ (space) has been added
# to our separators variable.

# > If I come over now and click on resume button. Next we should get a , (comma). That’s the one that’s just before
# the 775. Resume program, we’ve got a , (comma) in char now. If I step over you can see that’s added to our separators
# variable

# > Resume one more time, we should get the ; (semicolon), which is before the 8 0 7, and there’s obviously no other
# characters. I will click on resume button. We’ve got the ; (semicolon) and step over once more and that’s been added
# to our separators variable.

# > The remaining three characters at this point are all numeric and that means that we shouldn’t get to line 6 again
# and resuming the program, which I’ll do now, should cause it to run through to the end. You can see that’s been the
# case there.

# > I press the resume program button. The program ended. We click over to the console now we can see the output on
# screen. We’ve got our separators printed out, followed by a list containing the 7 values in number.

# > You might want to step through the code a few more times, just to make sure you understand what it’s doing. And
# it’s a reminder. Don’t worry about lines 10 and 11. They’re quite advanced and won’t make much sense at this point
# in the course

# >In the next video, we’ll see how a code can handle values that a user types in. See you in the next video
print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")

# ----------------------------------------------------------------------------------------------------------------------

# 59. for loops Extracting Values from User Input

print(("-" * 20) + "59. for loops Extracting Values from User Input" + ("-" * 20) + "\n")
# > In this video, we’re gonna make a small change to our code and see how it handles numbers that a user enters at the
# keyboard.

# > Let’s just remind ourselves about what this program is doing while running it
number = "9,223;372:036 854,775;807"
# We are binding an Empty String to separators variable
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)                               # ,;: ,;

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])             # [9, 223, 372, 36, 854, 775, 807]
print()

# > Basically, the separator is printed out on line 156, and the code produces a List of the 7 numeric values contained
# in the number variable on line 159. So that works fine.

# Q) Why have we bound "separators" variable to an “” (Empty String) on line 150?
# Let’s comment that line out and see what happens when we run it.

# > The first thing you’ll notice even before running the program is that we’ve got Warnings wherever the value of
# separators is used in the code. The code on line 180 is trying to take the Current Value of separators and Append the
# char to it. ***The problem is that Python has No Idea what the Current Value of separators is, and that’s because we
# haven’t bound separators to any value - it doesn’t exist.

# > If we hover over the warning on line 180, we can see “Name 'separators' can be undefined.

number = "9,223;372:036 854,775;807"
# separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
print()

# > We need to create the separators variable by attaching it to a value and that’s what we’re doing, effectively on
# line 176.
# > If I run the program now with line 176 still commented out, you can see we’re actually get a crash there:
# name 'separators' is not defined

# Output:
# Traceback (most recent call last):
#   File "C:\Users\coolh\OneDrive\Desktop\StudyMaterials\Python\python-masterclass-tim\programflow\SteppingThroughForLoop.py", line 180, in <module>
#     separators = separators + char
#                  ^^^^^^^^^^
# NameError: name 'separators' is not defined

# *** So basically, we need to define our separators variable by binding it to a value Before we try to use its value.
# So that’s really why line 176 is necessary.

# Let’s see how we can handle this code to get several values from the User.
number = input("Please enter a series of numbers, using any separators you like: ")     # 1, 23;456:789012
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)                               # , ::

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])             # [1, 23, 456, 789012]
print()

# > Let's run the program with user input of 1, 23;456:789012
# > Also, note that all the values I’ve entered have a different number of digits between different separators.
# ***That’s something that our Slice program Would Not have been able to handle.

# > When we press enter, we get a List containing the 4 values, [1, 23, 456, 789012]. Remember that we’re only
# interested in the “for” Loop at the moment. Again, don’t worry about understanding lines 213 and 214 at this time.

# > Let’s finish this video by making the program a bit more useful. Instead of just printing the values, I’ll get the
# program to Add them up and print out the Total.
# ***Python’s got sum() function built-in, and you can find a list of the built-in functions in the following link:
#       https://docs.python.org/3/library/functions.html
# > On line 240, we are going to change the code to calculate the sum by using sum() function

number = input("Please enter a series of numbers, using any separators you like: ")     # 1, 23;456:789012
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

# print(separators)                               # , ::

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))             # 789492
print()

# > Let's run the program with user input of 1, 23;456:789012
# > When we press enter, we get a value: 789492

# > Let's run the program with a different user input of 1,2 3;4: 5 6 7,8:9 10
# > When we press enter, we get a value: 55

# > The important bit about this code is the “for” Loop on lines 4 through 6. That iterates over the input and builds
# up a string containing anything that isn’t a numeric character.

# *** Because we’re extracting the separators from the user’s input, we don’t then have to care about what Separator
# Characters they’re using.

# > This code is already quite robust. Have a go at entering all sorts of input, and you’ll find it’s very difficult
# to crash the program. It is possible to crash it by holding down the control key, for example, but for normal input,
# it should cope with anything you can type. Moving forward, in the next video, we’ll look at iterating over another
# Iterable Type - the range. See you in the next video.

print(("-" * 20) + "End of the Topic" + ("-" * 20) + "\n")
