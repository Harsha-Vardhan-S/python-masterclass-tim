# Lets's start by binding a couple of labels to two int values.
a = 12
b = 3

# Lets create some expressions to see the basic Python arithmetic operators
print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 integer division, rounded down towards minus infinity
print(a % b)    # 0 modulo: the remainder after integer division
print()
# Note that although we’re using int values, division produces a float result 4.0 which you can see when the source code
# on line 9.
# Now, if you use two forward slashes // to perform integer division, then the result is an integer as you can see on
# line 10. We get 4 in this case. We got the expected result in this case.
# It can be important if we intend to use that value in a place where an int must be used.
# * For now, just make sure that you put four spaces before the word 'print', and a : colon at the end of the 'for' line
for i in range(1, 4):
    print(i)
print()
# The values we used In range on line 19 must be integers.

# So if we change this to a / b, we will get an error when we run it.
for i in range(1, a / b):
    print(i)
# We’ve got TypeError: 'float' object cannot be interpreted as an integer.

print()

# So performing integer division using two forward slashes // instead of one forward slash / would actually prevent this
# problem
for i in range(1, a // b):
    print(i)
# So essentially we change the code to perform integer division and the result of a // b is now an int. We’ll see
# another way to cope with situations like this. But for now, it’s something you need to be aware of.
# Python is strongly typed, and you can’t use a float in places where int must be used

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
