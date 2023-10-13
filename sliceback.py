# 33. Slicing Backwards
print(("-" * 20) + "33. Slicing Backwards" + ("-" * 20) + "\n")

# We have seen that you can use negative Start and Stop values in a Slice. You can also use a negative Step.
# There’s only one thing to watch out for, and it’s one of those things that’s obvious once it’s been pointed out.
# If I ask you to count backward from 99, and stop when you reach 100, how would you get on?
# You tell me it’s impossible, of course, and you can’t possibly get to 100 by carrying backward from 99. Well, neither
# can Python. Now that you know that you won’t make the most common error that people make when using negative Steps in
# a Slice.

# Create a new Python file called sliceback.py.
# Let’s see some examples.
#          01234567890123456789012345       # +ve Index start with 0 from left to right -->
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"      # 26 characters length
#          65432109876543210987654321       # -ve Index starts with -1 from right to left <--

backwards = letters[25:0:-1]
print(backwards)            # ZYXWVUTSRQPONMLKJIHGFEDCB
print()
# I’ve created a Slice that Starts at Index Position 25 which is the z, and I set the Stop value to Index Position 0
# and use the Step value of -1
# What do you expect the output to be here?
# We get the letters of the alphabet in reverse order from Z down to B. Notice that the letter A isn’t included. We used
# the Stop value of Index Position 0 and Slices extend up to, but not including the Stop value.

# Let’s review the code on line 17.
# ***When we’re using a Negative Step, the Start value MUST be Greater than the Stop value.
# Our slice starts at index position 25, and it extends down to index position 0 but doesn’t include the character at
# that position. We’re Stepping by -1 which produces all the letters from Z down to B.

# Second question: What Stop value will let the Slice include the letter A?
# There are two obvious answers to that, but only one of them works. So have a think and run your code to try your
# answers.

#          01234567890123456789012345       # +ve Index start with 0 from left to right -->
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"      # 26 characters length
#          65432109876543210987654321       # -ve Index starts with -1 from right to left <--

# Solution 1: Won't work
backwards = letters[25:-1:-1]
print(backwards)            # It won't print any output since Start value 25 & Stop value -1 refer to Z
print()

# If a Slice doesn’t include the position of the Stop value, is to use a Stop value of -1. But unfortunately, that’s
# the solution that doesn’t work.
# So, if we try that and use the Stop value of -1 and when we run it, we don’t get any output.
# Reason:
# Negative Stop values count backward from the end of the sequence. -1 means the last character in the string, which
# means we’ve requested a Slice that extends from the Z up to, but not including, the Z, and therefore we get nothing.

# Solution 2:
# The other obvious answer is to Omit the Stop value.
# Python will default to the Start or End of the sequence if we don’t specify the Start or Stop values when using
# Positive Step.
# So, it’s clever enough to work out that it should reverse the defaults when we’re using a Negative Step.
# (Jamba Lakidi Pamba) :P

backwards = letters[25::-1]
print(backwards)            # ZYXWVUTSRQPONMLKJIHGFEDCBA
print()

# ***With a Negative Step, the Start value defaults to the End of the string, and the Stop value defaults to the Start
# of the string.
# That means we can Omit our Start value as well.
# So if we go back and do that, and if we run it now, once again we get the string reversed.

backwards = letters[::-1]
print(backwards)            # ZYXWVUTSRQPONMLKJIHGFEDCBA
print()

# ***A Slice of [::-1] is a Python Idiom. When you see that, you’ll recognize it as Reversing the Sequence.
# I’ll cover a few more Slicing Idioms in the next video.

print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")
# Challenge:
# Using the “letters” string from the video, add some code to create the following Slices.
# Create a Slice that produces the characters QPO.
# Slice the string to produce EDCBA.
# Slice the string to produce the last 8 characters, in reverse order.
# ----------------------------------------------------------------------------------------------------------------------
# 34. Challenge Solution and Slicing Idioms
print(("-" * 20) + "34. Challenge Solution and Slicing Idioms" + ("-" * 20) + "\n")
#          01234567890123456789012345       # +ve Index start with 0 from left to right -->
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"      # 26 characters length
#          65432109876543210987654321       # -ve Index starts with -1 from right to left <--

# Create a Slice that produces the characters QPO.
qpoString = letters[16:13:-1]
print(qpoString)                # QPO
print()

# Slice the string to produce EDCBA.
# The easiest way to print the beginning of the string is to omit the Stop value
edcbaString = letters[4::-1]
print(edcbaString)
print()

# Slice the string to produce the last 8 characters, in reverse order.
# When using a Negative Step, the Start value defaults to the End of the string and therefore can be omitted
least8Characters = letters[:-9:-1]
print(least8Characters)         # ZYXWVUTS
print()

last8CharactersV2 = letters[25:17:-1]
print(last8CharactersV2)        # ZYXWVUTS
print()

# There are other solutions you could have used, especially when returning items from the Beginning and End of the
# sequence.
# Using default values for the Start and Stop is recommended when trying to return a certain number of characters from
# the Beginning or End of a sequence. If you manage to produce the correct strings with your Slices, well done.

# I’ll finish talking about Slices for now by looking at some common Python Idioms that Python programmers use and
# recognize.
# In the last video, I mentioned the Slice of [::-1]. is a Python idiom. When you see that, you’ll recognize it as
# reversing the sequence.

# Let’s see some more Python Idioms.
# The first is to return the last n items in a sequence.
# Let’s say we wanted the last 4 characters from the variable, letters
print(letters[-4:])         # WXYZ
print()
# Whenever you see a Slice with a Negative Start value and defaults for the Stop and Step [-n:], that just returns
# the end of the sequence.

# Our common use of that is to get the last item by specifying -1 for the Start value
print(letters[-1:])         # Z
print()

# You can also use a Slice to get the first character
print(letters[:1])          # A
print()
# The code on line 131 is particularly useful because it does not give an Error, even if the sequence is Empty.

# It may though, be more natural to get the item at Index Position 0, and that works with a string.
print(letters[0])           # A

# Q) Code on line 133 works, but what would happen if the string was Empty?

# Let's bind an Empty string to the variable, letters
letters = ""
print(letters[0])
# Output:
# File "C:\Users\coolh\OneDrive\Desktop\StudyMaterials\Python\python-masterclass-tim\HelloWorld\sliceback.py", line 138,
# in <module>
#     print(letters[0])
#           ~~~~~~~^^^
# IndexError: string index out of range

# As you can see, it generates an Index error when the string was Empty.

print(letters[:1])
print()
# So looking at the code, the Slice on line 151, produces an Empty string instead of Crashing with an Index error.
# So, the Python Idiom on line 148 is useful for getting the first item in a sequence, without your code crashing.
# ***If the sequence is Empty, you will get an Empty sequence back, and that’s often what you’d want to happen.

# That's the end of slices for now.

print(("-" * 20) + "End of Topic" + ("-" * 20) + "\n")
