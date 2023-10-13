# 36. String Replacement Fields
print(("-" * 20) + "36. String Replacement Fields" + ("-" * 20) + "\n")

# When printing strings and numbers, it would often be Convenient to display both values using a single call to print.
# For example, we might want to print a description of what a value is before the value itself.
# We’ve seen that Numbers can’t be concatenated with Strings using the + (Plus) Operator as the presence of a Number
# instructs Python to attempt Addition, and that fails.
# One approach we could take is to Coerce our Numbers into a String, using the str() function. In Python, every data
# type can be Coerced into a String representation.
# I mentioned that Java did this automatically, when an attempt is made to concatenate a String and a Number, and the
# same is possible with Python.

age = 24
print("My age is " + str(age) + " years")       # My age is 24 years
print()
# So, if we run the program, we confirm we get the output, “My age is 24 years” and we no longer get an error now,when
# we’re using the + (Plus) operator to concatenate Numbers and Strings.
# So, using the str() function helps us to basically Coerce an Integer into a String.
# But this can rapidly become tedious; having to coerce every variable using the string function.

# Python 3 provides a much better mechanism, and that has improved further in python 3.6.
# So python 3 allows strings to be formatted using Replacement Fields and the Dot Format Method.
# These are probably best explained with a few examples.
# So let’s rewrite the code on line 11. Instead of using the string function, we’re going to use
# {} (Replacement Fields) and the .format() (Dot Format) Method.
print("My age is {0} years".format(age))        # My age is 24 years
print()
# So this will produce the same output as the previous example, but without having to coerce the number into a string.

# So the Replacement Field is represented by the {0} which is then replaced by the first value in the format list age
# in this case, and at the moment, we’ve only got one value in there, and that’s the Variable, age.
# So that doesn’t look like much of an improvement over the previous code.

# Lets consider the following example instead:
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
# Output:
# There are 31 days in Jan, Mar, May, Jul, Aug, Oct and Dec
print()
# So I’ll split the code on line 35 over two lines, which is something you’ll see done a lot in Python. Long lines are
# actually frowned upon in the Python style guide, which we’ll talk more about later.
# 	For now, just know that Python allows you to split your lines of code
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
# Output: There are 31 days in Jan, Mar, May, Jul, Aug, Oct and Dec
print()
# So, the Replacement Fields are replaced by the values that appear in the .format method call, with the first value
# replacing {0}, the second replacing {1}, and so on. So, you can see that we’ve actually got a total of 8 Replacement
# Fields defined on line 37, and each of those values are going to go into the respective number 0 through 7.
# So we’ve got a total of 8 items in the list after the dot format, and each of those are going into the Replacement
# Field number 0 through 7 in our string.
# So if we run the program now and compare the output at the bottom of the screen with the values that appear inside
# the parenthesis after the .format() method call

# > So, in our code, we used 8 Replacement Fields numbered from 0 to 7.
# > These are replaced with the values in the parenthesis after the .format.
# > The first value goes into the replacement field {0}, the 2nd into {1}, and so on.
# > And that produces the output that we saw when we run the program
# > There are 31 days in Jan, Mar, May, Jul, Aug, Oct and Dec

# 	Of course, you probably wouldn’t use string literals inside .format, because, of course, they can just be included
# in the string.
# 	So, we could have, in this case, replaced what we did there on line 37, with something that’s probably a lot more
# readable.

print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec ".format(31))
print()

# 	***The other thing to keep in mind is that Replacement Fields can be used more than once, and they don’t have to
# appear in the order that the values are provided to the dot format method call.
# 	It’s the field Index, the number inside the curly braces that determines which value to be used.
# 	So here’s an example to demonstrate that
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {1}, Sep: {1}, Oct: {2}, Nov: {1}, "
      "Dec: {2}".format(28, 30, 31))
# Output: Jan: 31, Feb: 28, Mar: 31, Apr: 30, May: 31, Jun: 30, Jul: 31, Aug: 30, Sep: 30, Oct: 31, Nov: 30, Dec: 31
print()
# 	If we run the program, and you can see now that wherever there’s a replacement field {0}, it’s replaced with the
# first value in the list. 28. We’ve only got replacement field {0} once for February.
# 	All the replacement field {1} are replaced with the 2nd value, which is 30 and the 3rd value 31 is used to replace
# all the replacement field {2}.

# 	We can also use “““ ””” (Triple quotes).
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {1}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))

# Output:
# Jan: 31
# Feb: 28
# Mar: 31
# Apr: 30
# May: 31
# Jun: 30
# Jul: 31
# Aug: 30
# Sep: 30
# Oct: 31
# Nov: 30
# Dec: 31

# 	So now, if we run that, looking at the output for this program, each month appears on a new line and the number of
# days is also showing on there as well.
# 	This would be very difficult or would be very messy to reproduce with String Concatenation.
# 	Now if we would want to use Replacement Field {3} in the string, then we’d have to provide another value in the
# .format method call
