# 37. String Formatting
# 	String Replacement Fields can also contain formatting, to display values with a specific number of decimal places
# for example.
# 	Let’s create a new Python file and name it formatting.
# 	I’m going to use a For loop to generate some output. We’ll be looking at For loops in the next section, so don’t
# worry about what’s happening.
# 	Concentrate on the print lines that I’m going to type in this code, to see the effect of the formatting in the
# Replacement Fields.

# 	We’re going to start by printing the values from 1 to 12 with the values of their Squares and Cubes.

for i in range(1, 13):      # *** Put a : (colon) to the right of the ) (right parenthesis)
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

# *** You need to make sure there’s 4 spaces before print function

# 	***You can Provide Any Expressions Inside the .format Parenthesis. They don’t have to
# be variables or literal numbers.
# 	On line 12 we’ve got i **2 ( ** is called Exponent operator) to get the number squared and i ** 3 to get the number
# cubed.
# 	The ** (exponent operator) is how you can raise one number to the power of another in Python. That’s also referred
# to as Power To operator as well
print()

# Output:
# No. 1 squared is 1 and cubed is 1
# No. 2 squared is 4 and cubed is 8
# No. 3 squared is 9 and cubed is 27
# No. 4 squared is 16 and cubed is 64
# No. 5 squared is 25 and cubed is 125
# No. 6 squared is 36 and cubed is 216
# No. 7 squared is 49 and cubed is 343
# No. 8 squared is 64 and cubed is 512
# No. 9 squared is 81 and cubed is 729
# No. 10 squared is 100 and cubed is 1000
# No. 11 squared is 121 and cubed is 1331
# No. 12 squared is 144 and cubed is 1728

# 	We’ve got the values of the number, the value squared and the value cubed for each of those numbers.
# 	But as you can see, in the output the values rather aren’t lined up.
# So we can fix the output by applying some Formatting.

# 	First, we are going to specify Field Width for each of the Replacement Fields.
# 	All the values for i are a maximum of 2 digits because we are obviously counting from 1 to 12 here. So, we can use
# a Field Width of 2 for the first Replacement Field.
# 	We are going to use a Field Width of 4 for the other two Fields.
# 	To actually specify width, we add the width by putting a : (colon), and then the Field Width number that we need.
for i in range(1, 13):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))
print()
# Output:
# No.  1 squared is    1 and cubed is    1
# No.  2 squared is    4 and cubed is    8
# No.  3 squared is    9 and cubed is   27
# No.  4 squared is   16 and cubed is   64
# No.  5 squared is   25 and cubed is  125
# No.  6 squared is   36 and cubed is  216
# No.  7 squared is   49 and cubed is  343
# No.  8 squared is   64 and cubed is  512
# No.  9 squared is   81 and cubed is  729
# No. 10 squared is  100 and cubed is 1000
# No. 11 squared is  121 and cubed is 1331
# No. 12 squared is  144 and cubed is 1728

# 	It’s now easy to understand because the formatting makes it easier to see at a glance what the values are.
# 	So that looks tidier. The values are now lining up nicely.
# 	So line 12 we’re using {0: 2} in our left and right curly braces for the first Replacement Field.
# 	2 is the Field Width, as I mentioned and it’s separated from the Index with a : (colon).
# 	Now, everything in that first column prints in a width of 2 characters. So think of it as reserving 2 spaces on
# the screen so that the one-digit values still line up with the 2 digit numbers, and you can see that happening there
# in the output.
# 	Now our squares also line up, in a field width of 4 characters.

# 	Maybe with the 3 would look better there. Have a go at changing that yourself and see what it looks like.
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
print()
# Output:
# No.  1 squared is   1 and cubed is    1
# No.  2 squared is   4 and cubed is    8
# No.  3 squared is   9 and cubed is   27
# No.  4 squared is  16 and cubed is   64
# No.  5 squared is  25 and cubed is  125
# No.  6 squared is  36 and cubed is  216
# No.  7 squared is  49 and cubed is  343
# No.  8 squared is  64 and cubed is  512
# No.  9 squared is  81 and cubed is  729
# No. 10 squared is 100 and cubed is 1000
# No. 11 squared is 121 and cubed is 1331
# No. 12 squared is 144 and cubed is 1728

# We can also align the values in the Field Width. To Left align the values, place a < (less than symbol) after
# the : (colon).
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
print()
# Output:
# No.  1 squared is 1   and cubed is 1
# No.  2 squared is 4   and cubed is 8
# No.  3 squared is 9   and cubed is 27
# No.  4 squared is 16  and cubed is 64
# No.  5 squared is 25  and cubed is 125
# No.  6 squared is 36  and cubed is 216
# No.  7 squared is 49  and cubed is 343
# No.  8 squared is 64  and cubed is 512
# No.  9 squared is 81  and cubed is 729
# No. 10 squared is 100 and cubed is 1000
# No. 11 squared is 121 and cubed is 1331
# No. 12 squared is 144 and cubed is 1728

# Output of the code on line 74
# No.  1 squared is   1 and cubed is    1
# No.  2 squared is   4 and cubed is    8
# No.  3 squared is   9 and cubed is   27
# No.  4 squared is  16 and cubed is   64
# No.  5 squared is  25 and cubed is  125
# No.  6 squared is  36 and cubed is  216
# No.  7 squared is  49 and cubed is  343
# No.  8 squared is  64 and cubed is  512
# No.  9 squared is  81 and cubed is  729
# No. 10 squared is 100 and cubed is 1000
# No. 11 squared is 121 and cubed is 1331
# No. 12 squared is 144 and cubed is 1728

# As we can see, the numbers are aligned to the left when compared to the Output of the code on line 74

# 	Let’s center the last column to see what that looks like.
# 	So instead of using the < (less than symbol) there, I’ll change that by using the ^ (caret symbol) instead.

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
print()

# Output:
# No.  1 squared is 1   and cubed is  1
# No.  2 squared is 4   and cubed is  8
# No.  3 squared is 9   and cubed is  27
# No.  4 squared is 16  and cubed is  64
# No.  5 squared is 25  and cubed is 125
# No.  6 squared is 36  and cubed is 216
# No.  7 squared is 49  and cubed is 343
# No.  8 squared is 64  and cubed is 512
# No.  9 squared is 81  and cubed is 729
# No. 10 squared is 100 and cubed is 1000
# No. 11 squared is 121 and cubed is 1331
# No. 12 squared is 144 and cubed is 1728

#  If you run this code again, you can see the values are now clearly Centered compared to the first output, which
# was right justified on the right-hand side. This is obviously for the cubed values.
# 	Now keep in mind that we don’t get half spacing in a terminal. So the result isn’t as accurate as centering values
# in a GUI program, but it’s available if you want it.

# 	For floating-point numbers, you can specify a precision - the number of digits after the decimal point. For our
# precision, we specify the precision after a decimal point following the width field.
print("Pi is approximately {0:12}".format(22 / 7))      # Pi is approximately 3.142857142857143
print(len("142857142857143"))       # 15
print()
# 	The first line of output that is produced from the code on line 154, is the general format and that defaults to
# printing 15 decimals.
print("Pi is approximately {0:12f}".format(22 / 7))     # Pi is approximately     3.142857
print(len("    3.142857"))  # 12
print(len("142857"))        # 6
print()
# 	When we specify a floating-point value using the f on line 159, we get the default of 6 digits after the decimal
# point

# 	Now on lines 167 to 175, we’re still specifying a floating-point format, but we also add a precision of 50 and that
# gives 50 points (digits) after the decimal point.

print("Pi is approximately {0:12.50f}".format(22 / 7))
# Output:
# Pi is approximately 3.14285714285714279370154144999105483293533325195312
print(len("14285714285714279370154144999105483293533325195312"))    # 50
print()
# 	The output corresponds to line 167. If you think it doesn’t look right, that’s because Python won’t truncate a
# number. We can’t put a value that’s got 50 decimals in a field width of 12.
# 	Python decides that Precision is more important than Field Width and ignores the value 12 that we have specified for
# the width.

# 	Now, the next three lines after that, print the same value, but in different field widths. When we specify with
# greater than 50 you can see that the effect becomes clear.
# 	The maximum precision of a Python Floating-point number is between 51 and 53 digits. There’s not much point
# specifying a precision greater than that.

print("Pi is approximately {0:52.50f}".format(22 / 7))
# Output:
# Pi is approximately 3.14285714285714279370154144999105483293533325195312
print(len("3.14285714285714279370154144999105483293533325195312"))      # 52
print(len("14285714285714279370154144999105483293533325195312"))      # 50
print()

print("Pi is approximately {0:62.50f}".format(22 / 7))
print()
print("Pi is approximately {0:72.50f}".format(22 / 7))
print()


print("Pi is approximately {0:<72.50f}".format(22 / 7))
# Pi is approximately 3.14285714285714279370154144999105483293533325195312
print("Pi is approximately {0:<72.54f}".format(22 / 7))
# Pi is approximately 3.142857142857142793701541449991054832935333251953125000

# 	You can see, we only get one extra digit(5) in the output. We can see that there are 4 digits here, but the
# remaining digits are just padded with zeros. There’s no actual value there.

# So I’ll finish this video now by mentioning that
# 	***The field number in the Replacement Field is OPTIONAL. If they’re not specified, then Python takes the value
# from the .format method call in order.
# 	We are going to remove everything in the 3 Replacement Fields. We are going to leave {} only.
# 	For the 3rd Replacement Field, we will specify only the Width field {:4}
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
print()
# Output:
# No. 1 squared is 1 and cubed is    1
# No. 2 squared is 4 and cubed is    8
# No. 3 squared is 9 and cubed is   27
# No. 4 squared is 16 and cubed is   64
# No. 5 squared is 25 and cubed is  125
# No. 6 squared is 36 and cubed is  216
# No. 7 squared is 49 and cubed is  343
# No. 8 squared is 64 and cubed is  512
# No. 9 squared is 81 and cubed is  729
# No. 10 squared is 100 and cubed is 1000
# No. 11 squared is 121 and cubed is 1331
# No. 12 squared is 144 and cubed is 1728


# 	We can see that the 3rd Replacement Field shows that you can still use a colon to control the layout, even if
# you haven’t specified a field number. All the values in the final column of output are printed in a field width of 4.

# 	***Now, if you don’t provide field numbers, you can’t use a value more than once, nor can you change the order in
# which values are used.

# 	In our earlier example with the number of days in the month, wouldn’t have worked without field numbers.
# 	Experiment with different values for the field widths and precisions to see how it affects your output. And I’ll
# see you in the next video
