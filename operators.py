# 24. Numeric Data Types in Python

# So far, we have briefly discussed data types. In this video, we’ll look at Python types in more detail.
# Python has several built-in data types, that can be classified as:
#   1.Numeric
#   2.Iterator
#   3.Sequence (which are also iterators)
#   4.Mapping
#   5.File
#   6.Class
#   7.Exception

# We’ll be introducing all of these as the course progresses, but in the remainder of this section, we’ll have a look
# at the numeric data types and one of the sequence types.
# We’ve already seen the sequence type that I’ll discuss in this section: the str type, for strings.
# Before we look at that, I’ll start with the Numeric data types.

# Numeric Data Types
# Python 3 has three numeric data types:
# 1.	int
# 2.	float
# 3.	complex

# Python 2 had another type, long, because its int type couldn’t store very large values. In Python 3, the int type
# replaces long
# We’re not going to discuss complex numbers (which contain a real and an imaginary part, based on the square root of
# minus one)
# If you understand complex numbers, and want to use Python to manipulate them, then by the end of the course, you’ll
# understand Python well enough to be able to do so.
# Complex number theory is an advanced branch of mathematics and engineering, and we’re not going to attempt to explain
# it here.

# Integer & Float Data Types:
# The Python integer data type is called int.
# Integers are just whole numbers - numbers having no fractional part; whereas float is another name for real numbers -
# numbers having a fractional part after the decimal point.
# Integers can be considered just special cases of real numbers - but when represented in a computer, computations using
# integers that significantly faster than using floating point numbers.

# That’s one of the main reasons for the distinction in programming languages.
# Because of the way the integers are generally stored in the computer’s memory, many programming languages have a limit
# to the size of an integer - about 9 trillion in European terms, or 9 quintillion in American.
# ***The Python 3 int effectively has no maximum size.
# I’ll repeat that the programmers who are coming to Python from other languages: There’s no limit to the size of the
# values that you could store in a Python int. You’ll run out of memory before you exceed the size limit - because there
# isn’t one.

# Floating point numbers, or floats, are used to represent numbers having a fractional part.
# The Python floating point type is called float, and some examples of floating point numbers are:
# 1.0
# 123 .456
# 3.1515926 etc

# The maximum float value on a 64-bit computer is 1.7976931348623157e+308 which means moving the decimal point 308
# places right.
# The smallest float number is 2.2250738585072014e-308, which has 307 zeros after the decimal point.
# Python floats have 52 digits of precision, which should be adequate for most purposes. If you need more precise
# decimal numbers, Python 3 now includes a Decimal data type, but we won’t be using it in this course.
# In the later section, I’ll be showing you one trick you can use, to avoid rounding errors in financial calculations.

# Because Python doesn’t have type declarations (where you specify the type of a variable before you can use it), it’s
# tempting to think that you don’t have to understand the difference between the int and float types.
# But it is something you need to consider when writing your programs.
# That will make more sense when we look at some of the operations that can be performed on numbers, so let’s switch
# back to the IDE and do that, in the next video.

print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")

# ----------------------------------------------------------------------------------------------------------------------

# 25. Numeric Operators

# Lets's start by binding a couple of labels to two int values.
a = 12
b = 3
# Whenever we use the variable name, a, Python knows that it refers to the value 12. Similarly, variable name, b will
# refer to the value 3.

# Let's create some expressions to see the basic Python arithmetic operators
print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 integer division, rounded down towards minus infinity
print(a % b)    # 0 modulo: the remainder after integer division
print()
# Note that although we’re using int values, division produces a float result 4.0 which you can see when the source code
# on line 83.
# Now, if you use two forward slashes // to perform integer division, then the result is an integer as you can see on
# line 84. We get 4 in this case. We got the expected result in this case. So that can be important if we intend to use
# that value in a place where an int MUST be used.

# We are going to write a code to print the number 1 2 3
# Now don't worry about understanding this next bit of code.We are going to discuss "for" loops in detail in the next
# section of this course.
# * For now, just make sure that you put 4 spaces before the word 'print', and a : (colon) at the end of the 'for' line

for i in range(1, 4):
    print(i)
print()
# ***The values we used In range on line 98 MUST be integers.

# So if we change the stopping point of the range on line 98 from 4 to a / b, we will get a TypeError when we run it.
for i in range(1, a / b):
    print(i)
# Output:
# Traceback (most recent call last):
#   File "C:\Users\coolh\OneDrive\Desktop\StudyMaterials\Python\python-masterclass-tim\HelloWorld\operators.py",
#   line 104, in <module>
#     for i in range(1, a / b):
#              ^^^^^^^^^^^^^^^
# TypeError: 'float' object cannot be interpreted as an integer

print()

# So performing integer division using two forward slashes // instead of one forward slash / would actually prevent this
# problem
for i in range(1, a // b):
    print(i)
print()
# So essentially we change the code to perform integer division and the result of a // b is now an int. We’ll see
# another way to cope with situations like this. But for now, it’s something you need to be aware of.
# Python is Strongly Typed, and you can’t use a float in places where int must be used.
print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")

# ----------------------------------------------------------------------------------------------------------------------

# Expressions:
# In Python, an expression is anything that can be calculated to return a value.
# Lets's start by binding a couple of labels to two int values.
a = 12
b = 3
# a, b are not expressions. You can't have an expression on the left of an assignment.
# The expression on the right of the equals sign is evaluated and the variable on the left is bound to that result.

# Lets create some expressions to see the basic Python arithmetic operators
print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 integer division, rounded down towards minus infinity
print(a % b)    # 0 modulo: the remainder after integer division
print()

# What about i on line 58?
# Well, that’s also not an expression. i is being bound to each of the values produced by range in turn.
for i in range(1, a // b):
    print(i)
# So if I write this code long handed, instead of using for loop, it should become more obvious that i on line 58 is not
# an expression

i = 1
print(i)
i = 2
print(i)
i = 3
print(i)

# So that is exactly the same thing. But that would take six lines of code instead of 2 which I’ve got a lines 58, 59
# But when I run the programme we get the same three values printed out again.

# So i on the lines 63, 65, 67 isn't an expression, then it should be clear that it’s not an expression on line 58
# either

# 12 ... 1
# 3 ... 1
# a, b, a+b ... 3
#
# a, b, a-b ... 3
#
# a, b, a*b ... 3
#
# a, b, a/b ... 3
#
# a, b, a//b ... 3
#
# a, b, a%b ... 3
#
# range ... 1
#
# 1, a, b, a//b ... 4
#
# i (in print(i))... 1
#
# Total = 26


# 27. Operator precedence

a = 12
b = 3

# Operator Precedence is a fancy term for the Relative Importance given to each of the Operators. If they were all
# equally important, we could just read the expression on line 13 from left to right, and we’d get the result 12.
# A is 12 plus B, which is 3. This 15 / 3 is 5 – 4 These 1 * 12 = 12.
print(a + b / 3 - 4 * 12)       # -35.0

# However, multiplication & division have Higher Precedence than addition & subtraction. So those operations will be
# performed first. Now, many programming languages work in the same way. This isn’t just a peculiarity of python.
# So b / 3 is 1.0. And 4 * 12 is 48. So the expression, therefore, is evaluated as 12 + 1.0 - 48 which is -35.0.

# Now, if you want to make your expressions clear and unambiguous, you can use parentheses freely, even when python
# doesn’t specifically require them. So along those lines, we could revise our example from line 107 instead of type as
# follows:
print(a + (b / 3) - (4 * 12))       # -35.0
# In other words, both these expressions on lines 107, 116 evaluate to the same value.

# Now, if we had intended the early expression to produce the result 12, we would write it in a different way
print((((a + b) / 3) - 4) * 12)     # 12

print(((a + b) / 3 - 4) * 12)       # 12

# We could also use variables to hold the intermediate values if we wanted to
c = a + b
d = c / 3
e = d - 4
print(e * 12)

# So there will be times when it makes sense to break up an expression into smaller parts, as we’ve done here. I think
# in this example, the code is harder to read and difficult to workout what’s going on compared to the previous
# examples on line 48, 49, 50, 51, 52, 53 which are easy to read.
print()


# Ok, so I mentioned learning about operator precedence in school. Unfortunately, many schools use acronyms to help you
# remember the order evaluation. But the acronyms are ambiguous. Some common acronyms are:
# PEMDAS Parentheses, Exponents, Multiplication, Division, Addition, Subtraction.
# BEDMAS Brackets, Exponents, Division, Multiplication, Addition, Subtraction
# BODMAS Brackets, Order, Division, Multiplication, Addition, Subtraction
# BIDMAS Brackets, Index, Division, Multiplication, Addition, Subtraction

# Q) So what’s wrong with these acronyms?
# Well, they all have the same problem of being ambiguous. Students sometimes interpret them as meaning that
# Multiplication has higher precedence than division, and Addition has higher precedence than Subtraction.
# That’s not the case. Multiplication and Division have equal precedence, Addition and Subtraction also have equal
# precedence.
# In an expression that mixes operations with equal precedence they are evaluated from left to right.
print(a / (b * a) / b)      # 0.1111111111111111
