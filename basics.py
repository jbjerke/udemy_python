# Comments done with #

# Variables can be assigned together (not altogether that useful unless the
# variables are related)
all, at, once = 5, 10, 15
# all = 5
# at = 10
# once = 15

# CAN DO +=, -=, *=, etc

# integer division (//) to a float still leaves it as a float

# can change data types such as turning a float into an int using int(#)

# ================================================================
# Naming Restrictions
# ================================================================

# Start with either a letter or underscore
# _cats - good
# 2cats - bad

# Rest should only consist of letters, numbers, or underscores

# Naming Conventions =============================================
# snake-case: use underscores to separate things

# camel-case: likeThisOkay

# FOR PYTHON - common practive is snake-case

# Usually lowervase
# Constants can be done in all caps
# UpperCamelCase - usually refers to a class
# Variables with a double underscore are to be private/left-alone
# __no_touchy__

# ==================================================================
# Dynamic Typing
# ==================================================================
# Variables can change TYPES

# ==================================================================
# Quotes
# ==================================================================
# Either single or double quotes work but stick to the same one!

# ==================================================================
# String Escape Sequences/Characters
# ==================================================================
# \n for new line
# \" gives you double quotes in print out
# \\ gives a backslash when printed
# \/ doesn't do anything

# =================================================================
# Formatting Strings
# =================================================================
# To put numbers into a string, we use f-Strings
# So put an f in front of first quote(s) and then put the numbers in {}
# Math can be done in the {}

x = 10
oh_no = f"I've told you {x + 1} times already!"

print(oh_no)

# Indexing with strings: starts at 0 and uses []

# ======================================================================
# You can use input() to get user information
input("Enter your name here: ")

# ======================================================================
# Conditional Statements
# ======================================================================
# If Statements

#if something True:
#   do this
#elif something else is True:
#   do this instead
#else:
#   fallback to this

# we also have somthing called Truthiness or Falsiness
x = 1
#Truthy
x is 1 # True
#Falsy
x is 0 # False

# is vs ==
# == checks values
# is checks to see if the information is stored at the same address in memory
a=[1,2,3]
b=[1,2,3]
a==b #True
a is b #False

c = b
c is b #True

# => is only returns true if the variables point to the same address

# In lists, you have "in"
# something in a list

# Logical Operators:
# instead of && it's just 'if something and something'
# instead of || it's just 'if something or something'
# instead of !() it's just 'if not something'

# ===================================================================
# For Loops
# ===================================================================

# Syntax:
# for something in iterable object:
    #do something

# item - a new variable that interates through the object
# iterable object - the variable you are iterating through

for number in range(1, 8):
    print(number)

for ch in "coffee":
    print(letter)
    print(letter*10)

# =================================================================
# While Loops
# =================================================================

#while (boolean statement):
    # do this

# ===============================================================
# Controlled Exit
# ==============================================================
# The keyword "break" allows us to exit

# ================================================================
# List Methods
# ================================================================
# .append(elements) adds an element to the end of the list
# .extend([first element, ..., last element]) adds multiple elements to the end of the list
# .insert(pos, element) adds an element to a specific position pos of the list

# .clear()
# .pop() removes the last item
# .pop(pos) removes the item at the specified location
# .remove(value) removes the first instance of that value or throws a ValueError

# .index(value) returns the index of that item
# .index(value, start) gives back the index of value starting from the start point in the matrix til the end
# .index(value, start, end) gives back the index of value between the start and finish.
# .count(value) returns the number of times value occurs in the list
# .sort() sorts list in ascending order
# .reverse()

# "str".join(list) takes the strings in list and concatenates them with str in between each list entry

# =================================================================
# Slicing
# =================================================================
# taking a subset of the list
# list[start:end:step]
# can also use negative numbers
# can also do
# list[1:] take from 1 to the end
# can access whole list with just :
# list[:]

# list[:3] goes up til 3 (excludes 3 tho)

# ===============================================================
# Swap
# ===============================================================
#name[0], name[1] = name[1], name[0]

# ===============================================================
# List Comprehension
# ===============================================================
# nums = [1,2,3]
# [x*10 for x in nums]
# [10,20,30]
# it's a whole new list
# [bool(val) for val in [0,[]," "]]

# ===============================================================
# Dictionaries
# ===============================================================
#  Two ways to initialize
# var = {"string key" : value, int key : value, etc}
# var = dict(string key = value, int key = value, etc)

# Accessing:
# var[key] #gives value

# iterating
# using .values()

instructor = {
    "name" : "Colt",
    "owns_cat" : True,
    "num_courses" : 4,
    "favorite_language" : "Python",
    "is_hilarious" : False,
    44 : "my favorite number!"
}

for value in instructor.values():
    print(value)

""# can do the same using .keys() for the keys
# use .items() gives both keys and their respective values

for key,value in instructor.items():
    print(f"key is {key} and value is {value}"")

# Testing for the existance of a key in a dictionary
# just use in

"address" in instructor # False
"name" in instructor # True

# Methods :
# .clear() empties out dictionary
# .copy() creates a UNIQUE copy of the dictionary
    # i.e. "copyofdict is dict" returns false
# fromkeys create key-value pairs from comma separate values
{}.fromkeys("a","b") # {'a' : 'b'}
# Make a blank dict:
new_user = {}.fromkeys(['name','score','email','profile_bio'], 'Unknown')
# .get(key) returns value unless key is not in the dictionary
# .pop(key) removes the key and returns the value stored at that keys
# .popitem() removes a random key-value pair
# .update(dict) updates keys and values in a dictionary with another set of key-value pairs
first = dict(a=1,b=2,c=3,d=4,e=5)
second = {"a" = "amazing", f="damn"}

second.update(first) # second = dict(a=1,b=2,c=3,d=4,e=5,f="damn")
# if second has something in it, doing second.update({}) does nothing

# ================================================================
# Tuple
# ================================================================
# An ordered collection or grouping of items
# Main difference between it and a list is that it is immutable (cannot be changed)

# var = ( stuff1, stuff2, stuff3  )
# var = tuple(stuff1, stuff2, stuff3)
#example
alphabet = ('a','b','c','d')
alphabet.append('e') #error
alphabet[0] = 'A' #error

# to put one value in a tuple, you need a comma after the items
number = (1,)

# they can be used as keys in a dictionary
# example
locations = {
    (35.6895, 39.6917) : "Tokyo Office",
    (40.7128, 74.0060) : "New York Office",
    (37.7749, 122.4194) : "San Francisco Office"
}

# Looping
for letter in alphabet:
    print(letter)

# Methods
# .count(value) returns the number of times a value appears in the Tuple
# .index(value) returns the index at which a value is found in a Tuple

# ================================================================
# Sets
# ================================================================
# No order and no duplicates
# var = {stuff1, stuff2, stuff3}
# var = set({stuff1, stuff2, stuff3})

# if you try to initiate set with duplicates, the final result will still only show one

# Methods
# .add(value) adds a value
# if the value is already in the set, there is no error but it doesn't do anything

# .remove(value) removes the value if it is in there
# will throw an error if the value is not there

# intersection
# set1 & set2

# union
# set1 | set2

{x**2 for x in range(10)} #{0 , 1, 64, 4, 36, 9, 16, 49, 81, 25}

# ================================================================
# Functions
# ================================================================
# def name_of_function (input vars) :

# we can set one of the input variables to a value in the () as its default.

# We use """ """ to document functions and express the purpose of the function in it
# The document can be accessed useing .__doc__

# *arg as an input turns the inputs into a Tuple
# **kwargs stands for keyword args and turns the input into keywords in a dict

# to pass a list or tuple but to pass it as the separate items in the list, use start
# to unpack a dictionary into keywords, use **
