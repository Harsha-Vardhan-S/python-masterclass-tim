# 50. Using and, or, in Conditions

print(("-" * 20) + "50. Using and, or, in Conditions" + ("-" * 20) + "\n")

# > You’ll often want to test more complicated conditions than the simple ones we have used so far in the course. The
# good news is that Python lets us produce quite complex expressions.
# > Create a new file conditions.py in our project ProgramFlow
# > If we wanted to check if someone was of working age, we can test for their age being between 16 and 65, for example.
# > Now that would get a bit messy if we tested for their age being greater than equal to 16 and then used another test
# to see if it was less than equal to 65, *but we can perform both tests in one conditional expression.

# Let’s have a look at the code

age = int(input("How old are you? "))

if age >= 16 and age <= 65:
    print("Have a good day at work")

# > So here, if age is greater than equal to 16 and it also less than equal to 65, then the message on line 17 is going
# to be outputted.
# *** Notice that we have to repeat “age” in the expressions on line 16. What we have here is a complex expression made
# up of two simpler expressions:
# Expression 1: Firstly, we’ve got the expression age greater than equal to 16.
# Expression 2: Then we've got another expression, age less than equal to 65.
# > So either one of those expressions can evaluate to true.
# >The complete expression will ONLY be TRUE with BOTH parts TRUE. That’s because we use the word “and”

# Using or:
# > On the other hand, the question may have been phrased as:
# Q) Would you like an uncomfortable seat or an ice cream?
# > That allows you to choose either one of the options.
# ***This analogy falls down slightly, because, in English, there’s an implication that you can only have one or the
# other.
# *** In programming languages, BOTH conditions could be TRUE.

# Let’s see the possible results of evaluating expressions using “and” compared to using “or”
# and Truth Table:
#           True        False
# True      True        False
# False     False       False

# > To find out the results of using "and" with 2 conditions, read the value at the 2 values that are being "ANDed"
# together

# or Truth Table:
#           True        False
# True      True        True
# False     True        False

# The “or” truth table works in the same way, but the results will be different, of course.
# > To find the result of using “or” with 2 conditions, read the value of the intersection of the 2 values that are
# being “ORed” together.

# > That’s how “and” works, and also we had a brief discussion of “or”, which will be coming up in more detail.
# *** Both parts of the condition for “and” though, must be true for the overall condition to evaluate to true.
# > I’m gonna run the program now and we will test that with various inputs, just to make sure it works as we think it
# should.

age = int(input("How old are you? "))

if age >= 16 and age <= 65:
    print("Have a good day at work")

# > To test it fully, we should check the code for 5 different values (32, 12, 78, 16, 65)

# > For value 32, the “if” condition evaluates to true. Hence code on line 62 will be executed, printing out the
# message, Have a good day at work

# > Next, we need to test the code for a value less than 16. Let's test at value 12. The “if” condition fails and
# hence the code on line 62 won't be executed. Hence, we’ve got no output there.

# > Next, we need to test the code for a value greater than 16. Let's test at value 78. The “if” condition fails and
# hence the code on line 62 won't be executed. Hence, we’ve got no output there.

# > Next, we need to make sure the code works when we enter 16 or 65.
# > For value 16, the “if” condition evaluates to true. Hence code on line 62 will be executed, printing out the
# message, Have a good day at work

# > For value 65, the “if” condition evaluates to true. Hence code on line 62 will be executed, printing out the
# message, Have a good day at work

# > In the next video, we’re going to have a look at the suggestion that I’ve got from IntelliJ on line 61.
# It says, Simplify chained comparison. We’ll talk about that in the next video.

print(("-" * 20) + "50. Using and, or, in Conditions" + ("-" * 20) + "\n")

# ----------------------------------------------------------------------------------------------------------------------

# 51. Simplify Chained Comparison

print(("-" * 20) + "51. Simplify Chained Comparison" + ("-" * 20) + "\n")

age = int(input("How old are you? "))

if age >= 16 and age <= 65:
    print("Have a good day at work")

# > Let’s look at simplifying chained comparisons. The code on line 95, if you check carefully, is underlined with the
# squiggly line, which IntelliJ and PyCharm do when they have a Suggestion about your code. So, if we hover our mouse
# over that, you can see that it’s saying, “Simplify chained comparison”.

# > When dealing with numerical values in a condition, you can often replace “and” with a simpler comparison.
# > So what I’m going to do is comment lines 95 and 96. We’re going to make this a bit simpler instead by typing:
# if 16 <= age <= 65:

age = int(input("How old are you? "))

if 16 <= age <= 65:
    print("Have a good day at work")

# > I think that’s much easier to understand now because it’s obvious that age is in the range of 16 to 65. The
# condition is the same as the previous one, but it’s phrased in a more understandable way.
# > We should still test, it though, so if I run the program and repeat the inputs that we’ve used previously.
# > So when we ran it previously, we tested a value between 16 and 65. I’ll enter 32. That’s working ok. I’m getting
# the message printed out.
# > Next, if we run it again, we tested a value less than 16 and a value greater than 65. So it’s 12 the first test,
# and nothing’s printed out, which is correct.
# > Run it again. This time I’m going to enter 78. No output again. So that’s correct.
# > The final 2 tests were to make sure the code works when we enter 16 is 65.
# > I’m going to do that one at a time.
# > 16 works. 65 that also works. That’s working fine.

# > We could also turn the condition around or use “or” instead. As I’ve said a few times, there are often several ways
# to get the same result when you’re programming.

# > Let’s make a change to the program now, so that it prints a message when the condition is False, in other words,
# if age is outside of the range 16 to 65. So we are going to put “else” in there on line 133

age = int(input("How old are you? "))
# if age >= 16 and age <= 65:
if 16 <= age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your free time")
print()

print("-" * 80 + "\n")

# Let’s write the code using “or” instead of “and”.

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")

# > Now if the age is less than 16, we’re printing the message, Enjoy your free time
# > The code will do the same thing if the other part of the condition is true, If age is greater than 65.
# > We’re using “or” on line 141, which means we’ll get that message if either of those conditions is true, as opposed
# to “and”, where they both need to be true.
# > If neither of them is true, we’ll get the message in the “else” block on line 146.

# > So let’s run the program for a value 16
# > We have entered 16, and you can see, we “Have a good day at work” printed twice

# > Both bits of code are doing the same thing.
# > If you recall when we used “and” that’s the code on line 130, both conditions had to be true.
# > With “or”, as you can see, on line  “Enjoy your free time” will be printed if either condition is true.

# > Generally, one way or the other will be more natural in some situations and which to use will depend on the context.
# There is one important difference, though, that’s useful to be aware of.
# *** When comparing conditions using “and”, Python will stop checking as soon as it finds a condition that is “False”.
# *** When comparing conditions using “or”, it’ll stop as soon as it finds one that’s true.
# > So looking at line 11, if age is less than 16, then Python DOESN’T have to check to see if it’s also greater
# than 65.
# *** This can be very important, and we’ll be coming back to that later. For now, it’s just something to be aware of.

# > I’m going to stop the video here and in the next one, you’re going to take a look at Boolean values. See you in
# the next video.

print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")
