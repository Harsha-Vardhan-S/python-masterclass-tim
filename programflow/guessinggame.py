# 45. More on if, elif and else

print(("-" * 20) + "45. More on if, elif and else" + ("-" * 20) + "\n")

# > So now that we’ve seen how to use the debugger to step through our code line by line, let’s explore “if” statements
# a bit more.
# > We are going to continue with the project ProgramFlow. We’re going to create a new Python file: guessinggame
# > Now I’m going to start this up very simply, but we’ll improve it as we go along.
# > First thing we’re going to start by binding a value to the variable, answer. Now, the answer will always be 5 at the
# moment and that’s a bit boring, but will improve the program later.

answer = 5
# > Next, I want to print a prompt to let the user know what they’re entering, and then we’ll use the input() function
# to get their input.
print("Please guess number between 1 and 10: ")
guess = int(input())
# > Now I haven’t provided a prompt this time. We’re printing a message on line 15, which tells the player what the
# program is expecting them to do. Line 16 uses the input() function without a prompt, but we still need the opening
# and closing parenthesis after it.
# As before, we are using the int() function to convert their input to an integer. All input is stored as a string.
# But here we want to deal with numbers. So, on line 16, we’re binding the name, guess to the integer value that we’ve
# converted to an integer
# So, make sure you only have entered valid numbers when we run the program. We’ll be looking at how to cope with
# invalid input later in the course.

# > Now it’s time to see if the player’s guess was correct.
# > Now, here, when we run the program, there are 3 possible outcomes:
#   1. The guess could be too low.
#   2. The guess could be too high.
#   3. They could have guessed it correctly.
if guess < answer:
    print("Please guess higher")
elif guess > answer:
    print("Please guess lower")
else:
    print("You got it first time")
print()
# On line 31, we want to first test if the guess is too low.
# So basically, if a guess is less than the answer, we print a message asking them to guess higher.
# Now there’s a bit more we need to do here, but we’ll come back to that.
# Let’s add a test for the guess being too high. We can do that using elif condition on line .

# > Now, you might think that we can just use “if” on line , and you often can, but I’m going to discuss why that’s
# sometimes not a good idea, shortly.
# > If the condition on line 31 is false, the condition on line 33 is tested, and if that evaluates true, in other
# words, if their guess is greater than the answer, then we print the message, “Please guess lower”.
# > So that’s 2 of the 3 possible outcomes dealt with. We’re checking for the guess being less than the answer if it
# being greater than the answer so far.
# > If both those conditions are false, then the guess must be equal to the answer. In other words, they’ve guessed
# correctly. So, therefore we can handle everything else here using “else”.
# > So basically, the message on line 36 is only going to be printed in both the conditions on line 31 and line 33,
# evaluate to false.
# *** Because “else” picks up everything else, it must come after the “if” and “elif” blocks.
# *** elif must follow an “if”, and all “elif” blocks have to appear before the else block, if there is one.
# So let’s run the program a few times to check that it’s working for values (4, 8, 5)

# > Let’s run the code a few times, at different ages (4, 8, 5) just to make sure it is working as expected.
# > Firstly, try at 4, code on line 32 is executed. We got a message, Please guess higher.
# > If we try 8, code on line 34 is executed. we got the message, Please guess lower
# > If we try 5, code on line 36 is executed. We got a message saying, You got it first time

print(("-" * 20) + "End of the Topic" + ("-" * 20) + "\n")
# ----------------------------------------------------------------------------------------------------------------------

# 46. if, elif, and else in the Debugger
print(("-" * 20) + "46. if, elif, and else in the Debugger" + ("-" * 20) + "\n")

# > Let’s talk more about using if, elif and else in the debugger. At the moment, our program only allows 1 guess
# as its answer. Now we’re going to change that in an upcoming video.
# > But 1st let’s run it in the debugger, just to confirm what’s happening. We’re going to set a breakpoint on line 76.

answer = 5
print("Please guess number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher")
elif guess > answer:
    print("Please guess lower")
else:
    print("You got it first time")
# print()

# if / elif / else rules:
# > An “if” statement begins with the keyword "if", followed by a condition.
# > The “if” condition will always be evaluated.

# > Next, you can have one or more “elif” blocks.
# > You don’t have to include “elif” - and we will be seeing code that doesn’t.
# > But if you have any “elif” lines, then they come after the “if”.
# > “elif” also has to come before “else”, if there is an “else”.

# > Finally, you may have an “else” block.
# > You don’t have to use “else”, but if you do, it must come after the “if”.
# > It must also come after any “elifs”, if there are any.

# > In the next video, we’re going to improve the program slightly. It’s still not going to be very exciting. We’ve
# got a few more things to learn first, but we must learn to walk before we can run. See you in the next video.

print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")
# ----------------------------------------------------------------------------------------------------------------------

# Coding Exercise 5: Using if with strings

print(("-" * 20) + "Coding Exercise 5: Using if with strings" + ("-" * 20) + "\n")

# Write a small program that assigns the name of 2 trees to 2 variables, called tree1 and tree2.
# >If the values of the 2 variables are equal, print the message The trees are the same, otherwise print The trees
# are different.
# Note: This exercise system doesn't allow input to be used, so don't use input on lines 1 and 2 - just enter your
# text inside the quotes for the 2 trees.

# Solution:
tree1 = "mango"
tree2 = "guava"

# add the code to compare the trees
if tree1 == tree2:
    print("The trees are the same")
else:
    print("The trees are different")

print(("-" * 20) + "End of Coding Exercise" + ("-" * 20) + "\n")
# ----------------------------------------------------------------------------------------------------------------------

# Coding Exercise 6: Simple condition

print(("-" * 20) + "Coding Exercise 6: Simple condition" + ("-" * 20) + "\n")

# Write a small program that assigns the value 5 to one variable, called x, and the value 7 to another, called y.
#
# Your program should then use an if statement to compare the values, and print out x is greater than y if x is greater,
# or x is smaller than y if y is greater. If x equals y, print out x equals y
#
# I know you don't really need a computer to tell you the result, but we're getting practice at writing if/elif/else
# statements.
#
# Once your program is working, copy and paste it into a new file in your IDE, and test it with different values for x
# and y.

x = 5
y = 7

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is smaller than y")
else:
    print("x equals y")

print(("-" * 20) + "End of Coding Exercise" + ("-" * 20) + "\n")
# ----------------------------------------------------------------------------------------------------------------------

# 47. Adding a Second Guess
print(("-" * 20) + "47. Adding a Second Guess" + ("-" * 20) + "\n")

answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
else:
    print("You got it first time")

# Let’s revise our guessing game, specifically, what we’re going to do is give our players another guess, and we’ll do
# that by requesting input again.
# At the moment, we’ve got the code on line 162, which tests where the guess is less than the answer, and then we print
# a message, “Please guess higher”.
# We’re going to add some code on line 164 and this line must be indented at the same level as line 163. Both lines are
# part of the same code block and are indented to the same level.
# At this point, we’ve got a second guess from the player. The next step is to see if that guess was correct or not. So
# we’re going to add some code in line 165, 166
# So we’re comparing guess to answer to see if they got the correct answer. Note that we have to use two == (equal)
# symbols here, one on line 165.
# A single = (equal) is used when binding a variable to a value, or when assigning a value to a variable if you prefer
# to think of it that way.
# *** When testing for equality, we use two == (equal) signs.
#  Ok, so that’s all we need to do
# We have used an “if” statement to check if they got the right answer.
# *** You don’t have to have “elif” and “else” in your “if” statements. The code would benefit from an “else” clause
# but will come back to that.
# So that’s the 2nd guess when the first guess was lower than the answer.

# We’ll do the same thing if the guess is higher than the answer. We’re going to add some code on line 169 and this
# line must be indented at the same level as line 168. Both lines are part of the same code block and indented to the
# same level.
# At this point, we’ve got a second guess from the player. The next step is to see if that guess was correct or not.
# So we’re going to add some code in line 170, 171
#
# Our “if” and “elif” blocks each contain, now, another “if” block. Specifically, that’s the blocks on Lines 165 to 166
# and also on Lines 170 to 171.
# The two “if” statements on lines 165, 172 are indented one level at the same level as the other lines in the same
# block, as you can see.
# Lines 166, 171 are indented on another level because they are in another block. Those lines will only be executed
# when the condition guess is equal to answer is True.
# Let’s check if this code works.
# Let’s run the code a few times, at different ages (9, 8, 5) just to make sure it is working as expected.
# Firstly, try at 9, elif code block on line 167 is executed. We got a message, Please guess lower.
# Now there are quite a few tests to do here, to check every possible path through the code.
# Let's correctly guess this time. Let’s enter 5 as the second guess i.e., enter 5. “If” Code block on line 170 is
# executed. We got a message, Well done, you guessed it
#
# If you are not sure why the message came from line 15 rather than line 10, then run the program in the debugger to
# check that.
#
# If we try 1, code block on line 162 is executed. We got a message, Please guess higher.
# Let's correctly guess this time. Let’s enter 5 as the second guess i.e., enter 5. “If” Code block on line 165 is
# executed. We got a message, Well done, you guessed it
#
# Q) The code is working when we guess correctly the second time, but what happens if we get the 2nd guess wrong? Let’s
# test that.
# I’m going to enter 1 again, the message, “Please guess higher” will be printed.
# *** Now I’m going to enter 9, and as you see, that’s not very helpful. The program’s terminated without telling us
# what happened.
# *** I wanted to show that you don’t have to use elif and else clauses, but we really should use “else” after “if”
# blocks on lines 165 & 170, to print out a message when the second guess is wrong.
# Let’s add the “else” code blocks after the “if” blocks on lines 165 & 170. So, if the second guess is wrong, the
# “else” code blocks will print a message, Sorry, you have not guessed correctly
#
# Also, pay careful attention to the Indentation. The “if” and “else” keywords must be indented to the same level.
# This now makes it very easy to see which “else” or “elif” goes with which “if”. The indentation is essential for
# Python to understand what we want it to do, but the added benefit is that it also makes the code easier for us to
# read.

answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")

# We’re going to run the program again now. And I’m just going to do the same thing. In my case, I’m going to enter 1
# as the first guess, and 9 as the 2nd guess. This time we’ve got a message, “Sorry, you have not guessed correctly”.
# So run the program yourself and experiment with different values for your guesses.
# The answer is always 5 which is a bit boring but has the advantage to make it easier to test the program, in other
# words, you know which messages to expect.
# In the next video, we’ll look at more of the conditional operators.

print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")

# ----------------------------------------------------------------------------------------------------------------------
# 48. Conditional Operators

print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")

answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")

# > Let’s talk more about Conditional Operators in Python. But before we look at other conditional operators,
# let’s review the code from the last video.
# > On line 276, we test to see if the original guess is less than 5. If it is, we print message, "Please guess higher"
# and allow 2nd guess.
# > If the original guess is not less than 5, then line 283, checks if it’s greater than 5 using “elif”. We allow 2nd
# guess if it’s greater than 5.
# > If neither of those conditions is true, then the guess must have been equal to 5. This is picked up by the final
# “else” on line 290. There are better ways to write code like this as we see shortly. We’ve duplicated exactly the
# same code in the “if” (276) and “elif” (283) blocks.
# > The duplicate lines are lines 278 to 282 and also 285 to 289. Whenever you see duplication like this happening,
# that's a good indication that it can be done better.
# > For now, though, this example has illustrated several important concepts

# Let’s talk about “if” blocks.
# > A block can be quite complex, including further “if” and “else” blocks (and much more) contained within it.
# > When testing for equality, we can’t use a single = (equal) symbol. The single = (equal) is used for assigning
# values to variables, so when testing for equality, we must use == (two equal) symbols.
# *** An “if” statement can include many “elIf” parts, but there can only be one “else”. “elif” is short for “else if”.
# > The “else”, if there is one, must come after all the “elif” blocks.
# *** Duplicating code is generally a bad idea – there’s almost always a better way.
#
# Conditional Operators:
# When testing conditions, we can use any of the value comparison operators.
# There are other types of comparisons we can perform, but we’ll focus on these 6 for now.
# The 6 value comparison operators are:
# Condition			            Symbol
# Less than			            <
# Less than or equal to		    <=
# Greater than			        >
# Greater than or equal to	    >=
# Equal to			            ==
# Not equal to			        !=

# *** Once again, remember that we test for equality using the == (2 equal symbols). That’s something you’ll forget at
# first, but you’ll get a syntax error if you use a single = (equal), which should remind you.

# Now we know how to test for “Not Equal”, we can simplify our program.

# Comments:
# > In IntelliJ IDE, you can comment on a Block of code using: ctrl / (slash) or command / (slash) on a Mac.
# > Comments are ignored by the Python interpreter and are there to document your code.
# > In this case, the comments prevent the code from being executed.
# > Generally, you should use them to explain why you’ve done something in a certain way, or as a reminder of certain
# conditions or variable states that may not be obvious by looking at the code.
# > Remember that you may come back to modify the code, weeks or months after you wrote it.
# > Documentation can be extremely helpful when you work on another programmer’s code for the first time, or come back
# to your own code after a gap.
# > In Python, comments start with a # (hash) symbol and can appear on a line of their own, or at the end of a line of
# code.
# > In Python, comments start with a # (hash) symbol and can appear on a line of their own, or at the end of a line of
# code.
# > You can’t place them in the middle of a line, though, and  # (hash) inside a string is treated just like any other
# character, and doesn’t indicate a comment.
# > If you want a comment to span several lines, then start each line with a # (hash).


answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:   # guess must be higher than answer
        print("Please guess lower")
    guess = int(input())      # 2nd Guess
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")


# > This code highlights the importance of indentation in Python. Our second guess on line 361 is at the same
# indentation level as the “if’ and “else” statement on line 357 and 359. It’s NOT DEPENDENT on either condition in
# other words
# *** We get a different message if the guess is greater than 5 or less than 5, but line 11 is Executed Regardless of
# The Outcome of The If-Else Clauses.

# > I’ve also added a comment to the code online 359. This makes it clear to any humans reading the code what’s
# happening.
# >If you were to read the inner block (357-365) in isolation, it may not be obvious that the guess must be greater
# than 5, rather than a greater than equal to, i.e. not less than 5.
# > The comment on line 359 draws attention to the fact that we would not have gotten to the inner block if guess is
# equal to 5.

# > You can often do the same thing in many different ways, and this is an example of doing that. This new code does
# exactly the same thing as the previous code on lines 271 through 291.
# > Now, this can often confuse new programmers, because there’s usually more than one way to do the same thing.
# > Both of these bits of code will produce exactly the same results when given the same inputs.
# > Of course, the code on lines 271 through 291 won’t do anything now, because they start with a # hash. In other
# words, it’s been commented out. They’re ignored when we run the program. But if they weren’t commented out, they
# would have produced the same results as the code we’ve now got on lines 351 through 367.

# > Let’s check that by running the program to make sure that it still works.
# > Let’s run the code a few times, at different ages (9, 5, 1) just to make sure it is working as expected.
# > Firstly, try at 9, "if" code block on line 359 is executed. We got a message, Please guess lower.
# > Now there are quite a few tests to do here, to check every possible path through the code.
# > Let's correctly guess this time. Let’s enter 5 as the second guess i.e., enter 5. “If” Code block on line 362 is
# executed. We got a message, Well done, you guessed it

# If we try 1, code block on line 357 is executed. We got a message, Please guess higher.
# > Let's correctly guess this time. Let’s enter 5 as the second guess i.e., enter 5. “If” Code block on line 362 is
# executed. We got a message, Well done, you guessed it

# > If we try 1, code block on line 357 is executed. We got a message, Please guess higher.
# > If we try 9, "else" code block on line 364 is executed. We got a message, Sorry, you have not guessed correctly
# >That’s working fine and produces exactly the same results as the previous, now commented-out code.

# > You may also want to set breakpoints around the code in the debugger. Remember to think about which lines should be
# executed before stepping over the conditions to verify your results.

# > Let’s finish this video now with a Challenge, and we’ll go with the solution to the challenge in the next video.
# > The challenge is to change the condition on line 356 to :
#           if guess == answer:		        (previously it was--> if guess != answer:)
# > So change it so it says, if guess == answer:, then change the program in the appropriate places to give the correct
# results. So that’s the challenge.
print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")

answer = 5
print("Please guess number between 1 and 10:")
guess = int(input())

if guess == answer:
    print("You got it first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:   # guess must be higher than answer
        print("Please guess lower")
    guess = int(input())

    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")

# > This is a third way to write the program, and it still does exactly the same thing. It’s just phrased differently,
# just like you can do with human languages.
# > Here we’re checking for a correct guess first. It doesn’t really matter which way round you do it. There’s no
# necessary correct way of doing it. We’re looking for the result here, or for the solution, so if you manage to get
# the solution, congratulations.

print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")
