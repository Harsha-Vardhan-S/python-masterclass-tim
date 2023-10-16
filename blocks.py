# # 41. Introduction to Blocks and Statements
# print(("-" * 20) + "41. Introduction to Blocks and Statements" + ("-" * 20) + "\n")
# # You can use Shift Tab to remove a level of Indentation.
# # If you want to indent again in a code block,press Tab key. IDE adds 4 spaces
# # When are inside a code block, IDE automatically adds correct number of spaces for us.
#
# for i in range(1, 13):
#     print("No. {} square is {} and cubes is {:4}".format(i, i ** 2, i ** 3))
# print("*" * 80)
# print()
#
# # Output:
# # No. 1 square is 1 and cubes is    1
# # No. 2 square is 4 and cubes is    8
# # No. 3 square is 9 and cubes is   27
# # No. 4 square is 16 and cubes is   64
# # No. 5 square is 25 and cubes is  125
# # No. 6 square is 36 and cubes is  216
# # No. 7 square is 49 and cubes is  343
# # No. 8 square is 64 and cubes is  512
# # No. 9 square is 81 and cubes is  729
# # No. 10 square is 100 and cubes is 1000
# # No. 11 square is 121 and cubes is 1331
# # No. 12 square is 144 and cubes is 1728
# # ********************************************************************************
#
# # > We can see we get the squares and cubes printed, followed by a line of asterixes.
# # So the block of code on line 6, inside the for Loop, execute 12 times, but we only get a single line of asterixes at
# # the end, and that's because line 7 isn't part of th block.
#
# # However, we can make the code on line 7, as part of the block by Tabbing it across
#
# for i in range(1, 13):
#     print("No. {} square is {} and cubes is {:4}".format(i, i ** 2, i ** 3))
#     print("*" * 80)
# print()
# # Output:
# # No. 1 square is 1 and cubes is    1
# # ********************************************************************************
# # No. 2 square is 4 and cubes is    8
# # ********************************************************************************
# # No. 3 square is 9 and cubes is   27
# # ********************************************************************************
# # No. 4 square is 16 and cubes is   64
# # ********************************************************************************
# # No. 5 square is 25 and cubes is  125
# # ********************************************************************************
# # No. 6 square is 36 and cubes is  216
# # ********************************************************************************
# # No. 7 square is 49 and cubes is  343
# # ********************************************************************************
# # No. 8 square is 64 and cubes is  512
# # ********************************************************************************
# # No. 9 square is 81 and cubes is  729
# # ********************************************************************************
# # No. 10 square is 100 and cubes is 1000
# # ********************************************************************************
# # No. 11 square is 121 and cubes is 1331
# # ********************************************************************************
# # No. 12 square is 144 and cubes is 1728
# # ********************************************************************************
#
# # > On line 33, we have tabbed it over, so it's now indented at the same level as code on line 32. Now its part of the
# # for Loop code block.
# # > Notice that we get a very different result this time.
# # > Both line are now part of the same block and therefore both line get executed 12 times.
# # > That's how we create a code block using the tab key to Indent the code.
# # *** We're also starting to see why we might want to do that. We get very Different Results when we include line
# # print("*" * 80) inside the block as shown in line 34 compared to having it outside the block as in line 7
#
# # > The code still won't make a lot of sense. But what are for and range? That's some of the things we'll be looking at
# # in the rest of the section.
#
# # But now that we have understand what code blocks are, we can start to use them in our code. We will make a start on
# # that when we look at telling Python how to make decisions, in the next video.
# print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")
#
# # ----------------------------------------------------------------------------------------------------------------------
# # 42. if Statements
# print(("-" * 20) + "42. if Statements" + ("-" * 20) + "\n")
#
# # > We have seen how we can store values in variables, and print them out.
# # > We’ve also looked at getting input from the keyboard, in the previous section in this course.
# # > We’ll now start getting Python to make Decisions, based on the values of variables and input.
#
# # Let's type in a new program
# name = input("Please enter your name: ")            # Please enter your name: Harsha
# age = input("How old are you, {0}? ".format(name))  # How old are you, Harsha? 32
# print(age)                                          # 32
# print(type(age))                                    # <class 'str'>
#
# # > 32 is shown on the output console
# # *** Note that we can use Replacement Fields in any string, including the one we’re using as a prompt to the input()
# # function.
# # *** The input() function on line 88, returns as str or String data type. We have to convert it to an int if we want
# # age to represent a number, rather than the string, and we do that with the int() function.
#
# # So modifying above code on line 88 to output an int by using int() function
# name = input("Please enter your name: ")                    # Please enter your name: Harsha
# age = int(input("How old are you, {0}? ".format(name)))     # How old are you, Harsha? 32
# print(age)                                                  # 32
# print(type(age))                                            # <class 'int'>
#
# # Using int() and input() together as shown on line 99, is very common when you want to get a number from the user.
# # ***It does have a serious problem though. Your code will CRASH, if you type anything that can’t be converted to an
# # integer. Now we’ll be looking at how to handle that later in the course. Until then, make sure you Only Enter Valid
# # Numbers when our programs expect a number.
#
# # Let’s see, what would happen if we do insist on typing something that’s not a number. I’ll type in the text “twenty”.
# name = input("Please enter your name: ")                    # Please enter your name: Harsha
# age = int(input("How old are you, {0}? ".format(name)))     # How old are you, Harsha? twenty
# print(age)
# print(type(age))
# # Output:
# # Traceback (most recent call last):
# #   File "C:\Users\coolh\OneDrive\Desktop\StudyMaterials\Python\python-masterclass-tim\programflow\blocks.py", line 111,
# #   in <module>
# #     age = int(input("How old are you, {0}? ".format(name)))     # How old are you, Harsha? twenty
# #           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# # ValueError: invalid literal for int() with base 10: 'twenty'
#
# # > You can see we’ve got an error for code on line 111. We’ll talk about how to fix that later in the course
#
# # > At this point, we can make some decisions based on the person’s age. So, let’s start by checking if they’re old
# # enough to vote. In many countries, including Australia, the legal age for voting is 18.
#
# # So let’s write some code:
# name = input("Please enter your name: ")                    # Please enter your name: Harsha
# age = int(input("How old are you, {0}? ".format(name)))     # How old are you, Harsha? 18
# print(age)                                                  # 18
# print(type(age))                                            # <class 'int'>
#
# if age >= 18:
#     print("You are old enough to vote")                     # You are old enough to vote
# print()
# # > We started with the Keyword, ‘if’ and followed it with a condition, age>=18. Notice the : (colon) that we placed at
# # the end of that line 133. That means we started a New code block and the IDE indented the next line for us
# # automatically.
# # > The indentation is very important. That’s how Python knows that we’re starting a New Block of code.
# # >  If the condition on line 133, is true, in other words, the age entered is greater than or equal to 18, then we’re
# # printing out the message, You are old enough to vote
#
# # > Let’s run the code a few times, at different ages (18,17, 52) just to make sure it is working as expected.
# # > Firstly, try at 18, we will get a message, You are old enough to vote.
# # > If we try 17. We get just the value, 17. We don’t get a message saying, You are old enough to vote.
# # > And lastly, try 50, we got the message, You are old enough to vote
# # *** Remember to type valid numbers, or you’ll get the error that we saw earlier in the video for line 111, if you’re
# # not using a number.
#
# # > What we’ve done there on line 133, that’s how to test a Condition in Python.
# # > Now, conditions can be a lot more complex than that, as we’ll see. We know that a : (colon) tells python to expect a
# # new code block. So line 134 is indented by four spaces.
#
# # > If age is less than 18, nothing happens, which is a bit Unfriendly. We can cater for that by adding an ‘else’ Clause
# # to our ‘if’ Keyboard.
# # > Now we don’t want anymore code inside the ‘if’ block, which means we remove the indentation on the else line 163
# # > If the person’s age is greater than or equal to 18, the first block of code on line 165 is executed, otherwise the
# # second code block on line 168 is executed, asking them to come back in a Number of years, when they’re 18
#
# name = input("Please enter your name: ")                    # Please enter your name: Harsha
# age = int(input("How old are you, {0}? ".format(name)))     # How old are you, Harsha? 18
# print(age)                                                  # 18
# print(type(age))                                            # <class 'int'>
#
# if age >= 18:
#     print("You are old enough to vote")                     # You are old enough to vote
# else:
#     print("Please come back in {0} years".format(18 - age))
#
# # > Let’s run the code a few times, at different ages (18,52,15) just to make sure it is working as expected.
# # > Firstly, try at 18, we will get a message, You are old enough to vote.
# # > If we try 50, we got the message, You are old enough to vote
# # > If we try 15, second code block on line 168 is executed. We got a message saying, Please come back in 3 years
#
# # > As we saw in the last video, a block contains several lines of code to execute. Let’s go ahead and add some code in
# # ‘if’ code block. Add 2nd line under line 187
# # > Because lines 187 and 188 are in the same block, in other words, they’re indented to the same level, we should find
# # that both messages will be printed if the age is greater than equal to 18.
# # > Let’s just run that to confirm that is the case
#
# name = input("Please enter your name: ")                    # Please enter your name: Harsha
# age = int(input("How old are you, {0}? ".format(name)))     # How old are you, Harsha? 18
# print(age)                                                  # 18
# print(type(age))                                            # <class 'int'>
#
# if age >= 18:
#     print("You are old enough to vote")                     # You are old enough to vote
#     print("Please put an X in the box")                     # Please put an X in the box
# else:
#     print("Please come back in {0} years".format(18 - age))
# print()
#
# # > There are often several ways to do the same thing when programming. It may seem natural to deal with the voters
# # first, but we can do that the other way around as well.
# # > So to see what I mean, I’m going to add some code.
#
# # Example 1:
# name = input("Please enter your name: ")                        # Please enter your name: Harsha
# age = int(input("How old are you, {0}? ".format(name)))         # How old are you, Harsha? 15
# print(age)                                                      # 15
# print(type(age))                                                # <class 'int'>
#
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18 - age))     # Please come back in 3 years
# print()
#
# # Example 2:
# name = input("Please enter your name: ")                        # Please enter your name: Harsha
# age = int(input("How old are you, {0}? ".format(name)))         # How old are you, Harsha? 15
# print(age)                                                      # 15
# print(type(age))                                                # <class 'int'>
#
# if age < 18:
#     print("Please come back in {0} years".format(18 - age))     # Please come back in 3 years
# else:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# print()
# # > Here in the Example 2, we’re doing things the other way around compared to the Example 1.
# # > We’re not dealing with the voters first this time. We’re dealing with people who aren’t old enough to vote first.
# #  These two examples show there’s another way of doing the same thing.
#
# # > When we run these 2 examples, we’re going to enter the Same value for age.
# # > We’ve got exactly the same output two times on lines 207, 217
# # > So the code that we added for Example 2, ultimately does the same thing, but it’s checking the conditions the other
# # way around.
# # > If the person is less than 18, we print the message asking them to come back. Otherwise, we print the two lines,
# # asking them to tick the box.
#
# # Q) Doesn’t it matter which way you phrase the conditions?
# # Well, in this example, it doesn’t. But in the next video, we’ll see why it can matter.
#
# print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")

# ----------------------------------------------------------------------------------------------------------------------

# 43. elif

print(("-" * 20) + "43. elif" + ("-" * 20) + "\n")

# Example 1:
name = input("Please enter your name: ")                        # Please enter your name: Harsha
age = int(input("How old are you, {0}? ".format(name)))         # How old are you, Harsha? 20
print(age)                                                      # 20
print(type(age))                                                # <class 'int'>

if age >= 18:
    print("You are old enough to vote")                         # You are old enough to vote
    print("Please put an X in the box")                         # Please put an X in the box
else:
    print("Please come back in {0} years".format(18 - age))
print()

# Example 2:
name = input("Please enter your name: ")                        # Please enter your name: Harsha
age = int(input("How old are you, {0}? ".format(name)))         # How old are you, Harsha? 15
print(age)                                                      # 15
print(type(age))                                                # <class 'int'>

if age < 18:
    print("Please come back in {0} years".format(18 - age))     # Please come back in 3 years
else:
    print("You are old enough to vote")
    print("Please put an X in the box")
print()

# Sometimes we need to check more than just 2 cases.
# Looking at the code from the last video, we’re testing to see if the age is greater than or equal to 18 on line 250
# and we test the opposite condition age less than 18 on line 263.
# In both cases, the condition can be either True or False. If it’s true, the code blocks on lines 251 and 252 and line
# 264 are executed.
# If the condition evaluates to False, the code in the else blocks executes.

# Python lets us test several conditions by using elif. So I’ll explain a couple of rules about elif in a moment.
# First, let’s see an example of using it.
# We are going to add another condition to the if statement, on line 286

name = input("Please enter your name: ")                        # Please enter your name: Harsha
age = int(input("How old are you, {0}? ".format(name)))         # How old are you, Harsha? 15
print(age)                                                      # 15
print(type(age))

if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")
print()
# > elif, is short for ‘Else If’. The code now checks to see if age is less than 18. If it is, the message on line 287
# will be printed.
# > If the age isn’t less than 18, Python checks the elif Condition on line 288. So that’ll evaluate to either true or
# false. If true, the message on line 289 will be printed.
# If the age doesn’t equal 900, the condition evaluates to false, and Python continues with the else on line 290.

# > Let’s run the code a few times, at different ages (11,900,20) just to make sure it is working as expected.
# > If we try at 11, code block on line 287 is executed. We got a message saying: Please come back in 7 years

# > If we try at 18,
# This time the 'if' condition on line 286 is evaluated to false and therefore line 287 didnt get executed.
# Python then checks the elif condition on line 288. This also evaluated to false and therefore line 289 didnt get
# executed
# Instead Python skipped to the 'else' block on 290. There's no more conditions to check and none of the ones that were
# checked were true, so we are left with else block. Lines 291 & 292 were executed. We got a message:
#           You are old enough to vote.
#           Please put an X in the box

# > If we try exactly 900, elif code block is executed. Hence, the line 289 is executed. We got a message:
#           Sorry, Yoda, you die in Return of the Jedi

# > So all that would be much easier to understand, if we could see the computer executing the code, line by line.
# > Well, as it happens, we can do that. In the next couple of videos, we’re going to have a look at the debugger
# that’s built into the IntelliJ IDEs.
# > We’re going to look at the IntelliJ PyCharm debugger in the next video. In the video after that, we’ll see how to
# do the same thing with the debugger that’s built into IDLE.

print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")

# ----------------------------------------------------------------------------------------------------------------------
