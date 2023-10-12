# 28. The str String Data Type
print(("-" * 20) + "28. The str String Data Type" + ("-" * 20) + "\n")
# We have used strings in earlier examples to print messages on the screen. Now we’re going to look at some of the other
# cool things you can do with them.

# So, open the HelloWorld project and create a new Python file.
# Name the file as strings2.py It’s alright to use digits in your file names but avoid starting the name with a digit.
# Later in the course, we’ll be seeing how one program can import code from another program, but some file names can
# cause problems with that. So, use the same rules that apply to Python variable names, and you won’t get any problems

# Strings are one of the Python sequence data types, which makes sense because they are a sequence of characters. We’ve
# seen how to Print them out and Concatenate strings together, but we can also pick out INDIVIDUAL CHARACTERS OR
# SUBSTRINGS.

# Here we’re binding the variable called parrot to the string Norwegian Blue, and then printing parrot.
#         01234567890123    # 14 Characters length
parrot = "Norwegian Blue"
print(parrot)               # Norwegian Blue


# We can also print Individual Characters from the string. The statement on line 18 prints the letter w
print(parrot[3])            # w

# Now that might seem odd, because w is the 4th letter of Norwegian Blue, but it’s usual for programming languages to
# start counting at 0 and not 1. So thus parrot[0] will print N.
# There are 14 characters in Norwegian Blue, numbered from 0 to 13
# Add a comment on line 16 to the code to show the Index position
# The character N is at position 0, and we’ve already seen that w is at Index position 3. The last character in the
# string, the E in Blue, is at position 13. So that gives 14 characters numbered from 0 to 13.

# If we try to print parrot 14 in square brackets, we’ll get--> IndexError: string index out of range
# print(parrot[14])
# Output:
#   File "C:\Users\coolh\OneDrive\Desktop\StudyMaterials\Python\python-masterclass-tim\HelloWorld\strings2.py",
#   line 32, in <module>
#     print(parrot[14])
#           ~~~~~~^^^^
# IndexError: string index out of range

# The number inside the Square Brackets [ ] on line 22, 32 is called an Index, and it’s used to index into the string.
# Also, notice that I’ve used Square Brackets [ ] on line 22, 32.

# ***There are 4 uses of Square Brackets [ ] in Python, and they all involve Accessing Individual Items in something.
# We’ll see them used again when we look at Dictionaries and Sets.

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
print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")

# ------------------------------------------------
# 29. Negative Indexing in Strings
print(("-" * 20) + "29. Negative Indexing in Strings" + ("-" * 20) + "\n")
# So let’s see some more things we can do with indexing, continuing with the strings2 program from the last video.
# We can index backwards in a sequence by using a Negative number. So parrot[-1] will get the last character e.
# So let’s try this out

parrot = "Norwegian Blue"
#         43210987654321    # 14 Characters length
print(parrot[-1])           # e will be printed after we run the program

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

# The mini challenge is to change the indexes on lines 90 through 95 to use negative indexing.
# We still want the message ‘we win’ to be printed as follows
# w
# e
#
# w
# i
# n

#         01234567890123    # 14 Characters length
parrot = "Norwegian Blue"
#         43210987654321    # -ve Index starts with -1 from right to left <--

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
print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")

# ------------------------------------------------

# 30. Slicing

print(("-" * 20) + "30. Slicing" + ("-" * 20) + "\n")

# Python sequence types let you create a slice. The only sequence type we’ve looked at so far is the string type.
# So let’s continue with our strings2 program.
# We can produce the Slice by providing three numbers separated by : (colons) --> [x:y:z].
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
# Alright, so getting back to our code, the slice on line 149 produces the characters from Index 0 up to,
# BUT NOT INCLUDING Index 6.

print(parrot[3:5])            # we

# we can get the first word by getting the slice from position 0 up to, but not including position 9.
print(parrot[0:9])            # Norwegian
print()

# When creating a slice, the first value is the position to START at. That's separated from the position to STOP at
# with a : (colon).
# ***But if you don’t provide a START value, you still need the :(colon). So we could write that slice that we’ve got on
# line 151 differently as follows:
print(parrot[:9])           # Norwegian
print()
# As you see, we get exactly the same result. This time, the only difference is we DIDN’T provide a START value.
# Basically, lines 163 and 170 do the same thing because the START value defaults to the start of the sequence if we
# don’t provide the START value in a slice.

# So let’s look at some slides to explain exactly what’s going on here
# So our first slice on line 149 was [0:6]. The slice starts at index position 0 and it extends up to, but not including
# position 6
# The next slice on line 160 was [3: 5] So the slice starts at index position 3 and it extends up to but not including
# position 5
# Then we have the slice [0:9]. This slice starts at index position 0 and it extends up to, but not including index
# position 9
# As seen on line 170, we can leave off the START value of 0, because the START defaults to the beginning of the
# sequence.
# ***The : (colon) is, however, NECESSARY, otherwise, we’d be specifying the single character at position 9.


# Mini task: Create a slice that returns the word “Blue”.
#         012345678901234     # 14 Characters length
parrot = "Norwegian Blue"
# To slice the word Blue from our string, we need to start at position 10 and extend up to position 14.
# And again, there’s no character at position 14. But remember that slices "extend up to, but not including",
# the STOP value.
print(parrot[10:14])    # Blue
print()
# We saw that we can leave out the START value, and it will default to the Start of the sequence. If we leave out the
# STOP value, then it defaults to the End of the sequence.
# Hence we can rewrite the line 194 as follows:
print(parrot[10:])      # Blue
print()
# ***It’s important to include the : (colon) that separates the START and STOP values. We haven’t provided a STOP value,
# but we still need the : (colon)  so that Python knows that we want to Slice.
# Without the : (colon), that would be an Index, and we’d get a single character at position 10

# I mentioned that there are four different things that [] square brackets are used for. Until now, we have [] for:
#   1.Indexing
#   2.Slicing.
# If you use square brackets for Slicing, you must have at least one : (colon) otherwise it’s, in fact, an Index and
# not a Slice.

# We’ll have a quick recap.
# If the first number in a Slice is omitted, the Slice will start from the beginning of the string.
# And if the 2nd number is omitted, it’ll run to the end of the string.
print(parrot[:6])           # Norweg
print(type(parrot[:6]))     # <class 'str'>
print()

print(parrot[6:])           # ian Blue
print(type(parrot[6:]))     # <class 'str'>
print()

# The Slice indices are defined such as string[:n] + string[n:], is the same as the Original String.
print(parrot[:6] + parrot[6:])      # Norwegian Blue
print()

#
# Question: What happens if we only have a : (Colon) in the Slice? --> [:] In other words, what will this produce?
print(parrot[:])        # Norwegian Blue
print()
# If you don’t provide a START value, the Slice starts at the beginning of the sequence. Since there’s no START value on
# line 228. So we start at the beginning.
# If you don’t provide a STOP value, the Slice extends up to the end of the sequence. We haven’t got a STOP value on
# line 228 either. So that means the Slice will start at the beginning and extend right up to the end. So if we run the
# program now, we get the complete string printed out.

# ***When dealing with Lists, a Slice like [:] that produces a copy of the entire original can be very useful.
# I’ve covered it now because we’re looking at START and STOP values in a Slice, and we’ll see some practical
# applications of it later in the course

letters = "abcdefghijklmnopqrstuvwxyz"

print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")
# -----------------------------------------------------
# 31. Slicing with Negative Numbers

# Let’s continue with the strings2 program.
# ***The START, STOP and STEP values in a Slice can also be Negative.

#         01234567890123    # 14 Characters length
parrot = "Norwegian Blue"
#         43210987654321    # -ve Index starts with -1 from left to right <--

print(parrot[0:6]) # Norweg

print(parrot[-4:2])
# Now, if we run this, we’ll find that this actually doesn’t print out anything. So it doesn’t print the two characters
# Starting -4 in from the end of the string. That’s because you can’t go backward from the Starting position.
# So instead we should write it as follows

print(parrot[-4:-2])        # Bl
print()
# Code on line 248 prints from Index -4 and that’s B, up to but not including the second to last character in the
# string, which is u.

print(parrot[-4:12])        # Bl
print()
# Code on line 253 also prints the same thing i.e Bl, but this time it’s interpreted as from Index -4 up to but not
# including Index position 12.

# There’s nothing tricky about Negative Slicing. They’re just counting from the End of the string instead of from
# the beginning.

print(parrot[-14:-8])       # Norweg
print("End of Topic of Negative Slicing")
print()
# ------------------------------------------------
# 32. Using a Step in a Slice

# So far, we’ve only been providing 2 values to our Slices, the START and STOP values. But Slices can also take a STEP
# value, which defaults to 1.
# So let’s see some examples before we discuss the syntax more formally

#         012345678901234
parrot = "Norwegian Blue"
print(parrot[0:6:2])    # Nre
print()
# So the Slice on line 274 starts from Index 0 which is the capital N extracting all the characters Up To, But Not
# Including Index 6 which is the i, in Steps of 2.

print(parrot[0:6:3])    # Nw
print()
# On the line 278, the slice STARTs at Index position 0, as before. It extends up to, (but not including) position 6.
# But this time we’re STEPping through the sequence in STEPs of 3.

number = "9,223,372,036,854,775,807"        # ,,,,,,
print(number[1::4])
print()
# Now this example doesn’t appear to be very useful, but it does illustrate using a STEP in Slices.
# So it STARTs at Index position 1 which is the 1st , (Comma) and it’s Slicing every 4th character.
# The list extends all the way to the end of the string, and that’s because we’ve omitted the STOP value.

# Earlier I said it didn’t appear to be useful, however, it can be.
# In order to show you how it’s useful, we’re going to have to use some things that we’ll be looking at later.
# I don’t like doing this generally, and I won’t be doing it often. But I think something like that slice will make
# more sense if you can see a practical application of it.

# So what I’m going to do is start by changing some of the Separators. At the moment, they’re all Commas, but it’s
# possible we may have to process a String that contains a mix of Separators.
# So what I’m going to do is I will use a mix of Commas, Semicolons, Colons, and Spaces.
# These are all the things you might find used as Separators when processing data.

number = "9,223;372:036 854,775;807"        # ,;: ,;
print(number[1::4])
print()
# So if we run this program again now, we see those changed Separators in the output.

# Q) So why is that useful?
# Well if that number string represents seven values that appear in a data file, we can use the Separator string to
# split out the seven values.

# Now, this is the bit that I don’t want you to worry about. Think of it as a demonstration.
# It’s all stuff that you’ll be learning about in later videos.

number = "9,223;372:036 854,775;807"        # ,;: ,;
# So what I’m gonna do is start by binding a variable by name "seperators" to the variable "number"
seperators = number[1::4]
print(seperators)
print()

# Now we can use the separators variable to split out the individual values. This is the interesting part
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])         # [9, 223, 372, 36, 854, 775, 807]
print()
# Now, I don’t expect that code on lines 320 and 321 to make sense. Again, I’m using it to demonstrate why extracting
# every third character from a string might be useful. As you work through the course, you’ll learn what this code is
# doing, and you’ll be able to write code like that for yourself.

# If we run this program, you can see the output is now showing us the 7 values that we’ve extracted from the string
# that we bound to the “number” variable on line 313. I think that’s pretty impressive when you consider it’s only a few
# lines of code. It’s very hard to come up with real-world examples when all we’ve covered so far in the course of
# variables, int, and strings, but hopefully, that demonstration has put the slice into a useful context.
