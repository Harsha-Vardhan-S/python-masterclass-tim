# 28. The str String Data Type
# We have used strings in earlier examples to print messages on the screen. Now we’re going to look at some of the other
# cool things you can do with them.
# So, open the HelloWorld project and create a new Python file.
# Name the file as strings2. It’s alright to use digits in your file names but avoid starting the name with a digit.
# Later in the course, we’ll be seeing how one program can import code from another program, but some file names can
# cause problems with that. So, use the same rules that apply to Python variable names, and you won’t get any problems
# Strings are one of the Python sequence data types, which makes sense because they are a sequence of characters. We’ve
# seen how to Print them out and Concatenate strings together, but we can also pick out INDIVIDUAL CHARACTERS OR
# SUBSTRINGS.

# Here we’re binding the variable called parrot to the string Norwegian Blue, and then printing parrot.
#         01234567890123    # 14 Characters length
parrot = "Norwegian Blue"
print(parrot)

# We can also print Individual Characters from the string. The statement on line 17 prints the letter w
print(parrot[3])    # w

# Now that might seem odd, because w is the 4th letter of Norwegian Blue, but it’s usual for programming languages to
# start counting at 0 and not 1. So thus parrot[0] will print N.
# There are 14 characters in Norwegian Blue, numbered from 0 to 13
# Add a comment on line 12 to the code to show the index position
# The character N is at position 0, and we’ve already seen that w is at index position 3. The last character in the
# string, the E in Blue, is at position 13. So that gives 14 characters numbered from 0 to 13.

# If we try to print parrot 14 in square brackets, we’ll get--> IndexError: string index out of range
#print(parrot[14])


# The number inside the Square Brackets [ ] on line 17 is called an Index, and it’s used to index into the string.
# Also, notice that I’ve used Square Brackets [ ] on line 17. There are 4 uses of Square Brackets [ ] in Python, and
# they all involve Accessing Individual Items in something. We’ll see them used again when we look at Dictionaries and
# Sets.

# Mini Challenge:
# Add some code to the program so that it prints out: we win
# Each character should appear on a separate line.
# * The program should get the characters from the parrot string using Indexing.
# The w is already printed out. You just need to print out the remaining 5 characters.
# With the text that is already printed, the final output from the program should be:
#
# Norwegian Blue
# w
# e
#
# w
# i
# n

print(parrot[4])        # e
print(parrot[9])        #
print(parrot[3])        # w
print(parrot[6])        # i
print(parrot[8])        # n

print()
print("End of Topic")
print()

# ------------------------------------------------
# 29. Negative Indexing in Strings

# So let’s see some more things we can do with indexing, continuing with the strings2 program from the last video.
# We can index backwards in a sequence by using a Negative number. So parrot[-1] will get the last character e.
# So let’s try this out

parrot = "Norwegian Blue"
#         43210987654321    # 14 Characters length
print(parrot[-1])       # e will be printed after we run the program

# *Note that minus zero doesn’t really make sense here. So when counting from the end of the string, we start counting
# from -1.

print(parrot[-14])      # N
print()

# Let's try a mini challenge

# print(parrot[3])        # w
# print(parrot[4])        # e
# print(parrot[9])        #
# print(parrot[3])        # w
# print(parrot[6])        # i
# print(parrot[8])        # n

# The mini challenge is to change the indexes on lines 80 through 85 to use negative indexing.
# We still want the message ‘we win’ to be printed as follows
# w
# e
#
# w
# i
# n

#         01234567890123    # 14 Characters length
parrot = "Norwegian Blue"
#         43210987654321    # -ve Index starts with -1 from left to right <--

print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

# You may notice that the negative index values can be obtained by subtracting the string length, 14 in this case,
# from the positive indexed numbers.
# So you may have done something like this, just basically subtracting 14 from each value.
#         012345678901234       # +ve Index starts with 0
parrot = "Norwegian Blue"       # 14 Characters length

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

print()
print("End of Topic")
print()

# ------------------------------------------------
# 30 Topic: Slicing
# Python sequence types let you create a slice. The only sequence type we’ve looked at so far is the string type.
# So let’s continue with our strings2 program.
# We can produce the slice by providing three numbers separated by : colons --> [x:y:z].
# These numbers are the Start, Stop, and Step values. We will deal with Step value later.
# But 1st let’s look at slicing without a step.

#         012345678901234     # 14 Characters length
parrot = "Norwegian Blue"

print(parrot[0:6])            # Norweg      # up to, but not including
# So here we’re telling python to start at position 0 and Slice up to, but Not Including, position 6

# So when I said NOT INCLUDING, that’s IMPORTANT and something that new Python programmers often forget.
# ***The last character you specify isn’t included in the slice.***
# It turns out that not including that last character makes slice as much easier to use, but it’ll probably catch
# you out at first.
# In fact, not including that final value is something that happens in other places in Python, such as RANGES.
# Alright, so getting back to our code, the slice on line 137 produces the characters from Index 0 up to,
# BUT NOT INCLUDING Index 6.

print(parrot[3:5])            # we

# we can get the first word by getting the slice from position 0 up to, but not including position 9.
print(parrot[0:9])            # Norwegian
print()

# When creating a slice, the first value is the position to START at. That's separated from the position to STOP at
# with a : colon.
# ***But if you don’t provide a START value, you still need the colon. So we could write that slice that we’ve got on
# line 151 differently as follows:
print(parrot[:9])           # Norwegian
print()
# As you see, we get exactly the same result. This time, the only difference is we DIDN’T provide a START value.
# Basically, lines 151 and 158 do the same thing because the START value defaults to the start of the sequence if we
# don’t provide the START value in a slice.

# So let’s look at some slides to explain exactly what’s going on here
# So our first slice on line 137 was [0:6]. The slice starts at index position 0 and it extends up to, but not including
# position 6
# The next slice on line 148 was [3: 5] So the slice starts at index position 3 and it extends up to but not including
# position 5
# Then we have the slice [0:9]. This slice starts at index position 0 and it extends up to, but not including index
# position 9
# As seen on line 158, we can leave off the START value of 0, because the START defaults to the beginning of the
# sequence.
# ***The : (colon) is, however, NECESSARY, otherwise, we’d be specifying the single character at position 9.


# Mini task: Create a slice that returns the word “Blue”.
#         012345678901234     # 14 Characters length
parrot = "Norwegian Blue"
# To slice the word Blue from our string, we need to start at position 10 and extend up to position 14.
# And again, there’s no character at position 14. But remember that slices "extend up to, but not including",
# the STOP value.
print(parrot[10:14])    # Blue

# We saw that we can leave out the START value, and it will default to the Start of the sequence. If we leave out the
# STOP value, then it defaults to the End of the sequence.
# Hence we can rewrite the line 182 as follows:
print(parrot[10:])      # Blue
print()
# ***It’s important to include the : (colon) that separates the START and STOP values. We haven’t provided a STOP value,
# but we still need the : (colon)  so that Python knows that we want to Slice.
# Without the : (colon), that would be an Index, and we’d get a single character at position 10

# I mentioned that there are four different things that square brackets are used for, and the slicing is the 2nd thing.
# They used for Indexing, and they used for Slicing.
# If you use square brackets for Slicing, you must have at least one : (colon) otherwise it’s, in fact, an Index and
# not a Slice.

# We’ll have a quick recap.
# If the first number in a Slice is omitted, the Slice will start from the beginning of the string.
# And if the 2nd number is omitted, it’ll run to the end of the string.
print(parrot[:6])
print(type(parrot[:6]))
print()

print(parrot[6:])
print(type(parrot[6:]))
print()

# The Slice indices are defined such as string[:n] + string[n:], is the same as the Original String.
print(parrot[:6] + parrot[6:])      # # Norwegian Blue
print()

#
# Question: What happens if we only have a : (Colon) in the Slice? --> [:] In other words, what will this produce?
print(parrot[:])        # Norwegian Blue
print()
# If you don’t provide a START value, the Slice starts at the beginning of the sequence. Since there’s no START value on
# line 215. So we start at the beginning.
# If you don’t provide a STOP value, the Slice extends up to the end of the sequence. We haven’t got a STOP value on
# line 215 either. So that means the Slice will start at the beginning and extend right up to the end. So if we run the
# program now, we get the complete string printed out.

# When dealing with Lists, a Slice like [:] that produces a copy of the entire original can be very useful.
# I’ve covered it now because we’re looking at START and STOP values in a Slice, and we’ll see some practical
# applications of it later in the course

letters = "abcdefghijklmnopqrstuvwxyz"

print("End of Topic")
print()
# -----------------------------------------------------

#         012345678901234
# parrot = "Norwegian Blue"
# print(parrot[0:6]) # Norweg
#
# print(parrot[-4:2])

#         012345678901234
parrot = "Norwegian Blue"
print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

number = "9,223,372,036,854,775,807"
print(number[1::4])

# number = "9,223;372:036 854,775;807"
# print(number[1::4])

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
