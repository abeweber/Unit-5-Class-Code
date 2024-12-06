"""
Name: Abe Weber
Date: 12/2/24
Topic: Strings
"""

# Review
name = "Starla" # a string literal
age = 5
# f-strings (formatted strings)
description = f"{name} likes wand toys and is {age}"

print(description)

# same result with concatenation
description = name + " likes wand toys and is " + str(age)
print(description)

# indexing = every character in a string has a location
# starting at 0 from the beginning or -1 from the end

# 0 1 2 3 4 5
# S t a r l a

first_letter = name[0] # always use 0 if you don't know length
print(first_letter)
first_letter = name[-6]
print(first_letter)
first_letter = name[-1*len(name)] # if you don't know length
print(first_letter)

last_letter = name[-1] # always use if you don't know length
print(last_letter)
last_letter = name[len(name)-1]
print(last_letter)

# use [ ] to access a character not ( ) - gives TypeError
# accessing an index that does not exist gives IndexError

#Slicing - used to access 1 or more characters in a string
# Instead of name[0]+name[1]+name[2] we can do name[0:3]

#first three letters
first_three = name[0]+name[1]+name[2]
print(first_three)
first_three = name[0:3] #start at index 0, go up to but not include 3
print(first_three)

# Format
# string_name[start:stop:step] - none are technically required

word_one = "Adventure"
# What is the result of print(word_one[3:])?
# Try leaving out start
# Try negative indices?

no_stop = word_one[3:]
print(no_stop)
no_start = word_one[:9]
print(no_start)
none = word_one[:]
print(none)
print(word_one[-3:])
print(word_one[:-3])
print(word_one[::-1])
print(word_one[-3:-7:-2])

#