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
